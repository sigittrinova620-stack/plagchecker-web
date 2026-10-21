"""
Crossref & Open Academic Similarity Fetcher
Queries public academic metadata and open-access abstracts for matching papers.
"""
import urllib.request
import urllib.parse
import json
import re

def search_crossref_academic(query_title: str, max_results: int = 3):
    """
    Searches Crossref API for academic papers with similar titles/abstracts.
    Returns list of reference dicts {title, content, filename}
    """
    clean_title = re.sub(r'[^a-zA-Z0-9 ]', ' ', query_title)
    encoded = urllib.parse.quote_plus(clean_title[:100])
    url = f"https://api.crossref.org/works?query.title={encoded}&rows={max_results}"
    
    headers = {"User-Agent": "TurnitinSimilarityClone/1.0 (mailto:scholar@example.com)"}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get("message", {}).get("items", [])
            docs = []
            for item in items:
                title = item.get("title", [""])[0]
                abstract = item.get("abstract", "")
                # Strip XML tags from Crossref abstracts if any
                clean_abstract = re.sub(r'<[^>]+>', '', abstract)
                container = item.get("container-title", ["Jurnal Publikasi"])[0] if item.get("container-title") else "Jurnal Ilmiah"
                
                content = f"{title}. {container}. {clean_abstract}"
                if len(clean_abstract) > 50:
                    docs.append({
                        "title": title or "Jurnal Ilmiah Terindeks",
                        "content": content,
                        "filename": "Internet/Journal Article"
                    })
            return docs
    except Exception as e:
        print(f"Crossref search warning: {e}")
        return []
