"""
Comprehensive Academic & Web Crawler (SINTA, Scopus, Google Scholar, OpenAlex, Crossref)
Fetches FULL-TEXT articles from:
- OpenAlex Open Access direct PDF URLs (250M+ global & Indonesian repository papers)
- Crossref DOI similarity-checking links (SINTA journals, Garuda, OJS)
- Title-matched and DOI-matched publisher downloads
"""
import urllib.request
import urllib.parse
import json
import io
import re
from typing import List, Dict, Any
from pypdf import PdfReader

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

def download_and_extract_pdf_text(pdf_url: str) -> str:
    """Downloads a PDF from a URL and extracts its text cleanly."""
    try:
        req = urllib.request.Request(pdf_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            pdf_bytes = resp.read()
            reader = PdfReader(io.BytesIO(pdf_bytes))
            pages_txt = [p.extract_text() or "" for p in reader.pages]
            return "\n".join(pages_txt)
    except Exception:
        return ""

def discover_all_published_sources(pages: List[str]) -> List[Dict[str, Any]]:
    """
    Scans the document for titles, DOIs, and keywords, then retrieves FULL TEXT
    from global academic repositories (SINTA, Scopus-indexed DOIs, OpenAlex OA).
    """
    discovered_sources = []
    seen_urls = set()
    first_pages_text = "\n".join(pages[:3])

    # 1. Check for DOI in text
    dois = re.findall(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', first_pages_text)
    for raw_doi in set(dois):
        clean_doi = raw_doi.rstrip('.,;) ]')
        try:
            url = f"https://api.crossref.org/works/{urllib.parse.quote(clean_doi)}"
            req = urllib.request.Request(url, headers={"User-Agent": "TurnitinAuditor/6.0 (mailto:scholar@univ.edu)"})
            with urllib.request.urlopen(req, timeout=4) as resp:
                item = json.loads(resp.read().decode('utf-8')).get("message", {})
                title = item.get("title", [f"Jurnal DOI: {clean_doi}"])[0]
                venue = item.get("container-title", ["Jurnal Publikasi"])[0] if item.get("container-title") else "Internet"
                
                # Check links
                for l in item.get("link", []):
                    link_url = l.get("URL")
                    if link_url and link_url not in seen_urls:
                        seen_urls.add(link_url)
                        body_text = download_and_extract_pdf_text(link_url)
                        if len(body_text.split()) > 100:
                            discovered_sources.append({
                                "title": title,
                                "source_name": f"{venue} (DOI: {clean_doi})",
                                "type": "Publication / Scopus / SINTA",
                                "content": body_text
                            })
                            break
        except Exception:
            pass

    # 2. Extract candidate titles from headings
    clean_lines = [l.strip() for l in first_pages_text.split('\n') if len(l.strip().split()) >= 4]
    candidate_queries = clean_lines[:5]

    for q in candidate_queries:
        # Search OpenAlex (Access to Scopus/SINTA indexed papers with direct OA full-text URLs)
        try:
            oa_url = f"https://api.openalex.org/works?search={urllib.parse.quote(q)}&per-page=2"
            req = urllib.request.Request(oa_url, headers={"User-Agent": "TurnitinAuditor/6.0 (mailto:scholar@univ.edu)"})
            with urllib.request.urlopen(req, timeout=4) as resp:
                results = json.loads(resp.read().decode('utf-8')).get("results", [])
                for work in results:
                    oa_link = work.get("open_access", {}).get("oa_url")
                    title = work.get("display_name", "")
                    venue = work.get("primary_location", {}).get("source", {}).get("display_name") or "Internet Repository / Jurnal"
                    
                    if oa_link and oa_link not in seen_urls:
                        seen_urls.add(oa_link)
                        body = download_and_extract_pdf_text(oa_link)
                        if len(body.split()) > 100:
                            discovered_sources.append({
                                "title": title,
                                "source_name": venue,
                                "type": "Internet / Open Access Journal",
                                "content": body
                            })
                            if len(discovered_sources) >= 5:
                                return discovered_sources
        except Exception:
            pass

    return discovered_sources
