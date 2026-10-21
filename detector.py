"""
Turnitin Exact Matching & Similarity Engine
Applies standard Turnitin sequence matching (3 to 5+ words) and phrase attribution.
"""
import re
import difflib
from pathlib import Path
from typing import List, Dict, Any

TURNITIN_PALETTE = [
    {"bg": "rgba(239, 68, 68, 0.45)", "solid": "#ef4444", "name": "Merah"},
    {"bg": "rgba(249, 115, 22, 0.45)", "solid": "#f97316", "name": "Oranye"},
    {"bg": "rgba(234, 179, 8, 0.45)", "solid": "#eab308", "name": "Kuning"},
    {"bg": "rgba(34, 197, 94, 0.45)", "solid": "#22c55e", "name": "Hijau"},
    {"bg": "rgba(14, 165, 233, 0.45)", "solid": "#0ea5e9", "name": "Biru"},
    {"bg": "rgba(139, 92, 246, 0.45)", "solid": "#8b5cf6", "name": "Ungu"},
    {"bg": "rgba(236, 72, 153, 0.45)", "solid": "#ec4899", "name": "Pink"},
    {"bg": "rgba(16, 185, 129, 0.45)", "solid": "#10b981", "name": "Emerald"},
]

def clean_tokens(text: str) -> List[str]:
    return [w.lower() for w in re.findall(r'\b[a-zA-Z0-9\u00C0-\u024F\u1E00-\u1EFF\-]{2,}\b', text)]

def compare_document_with_sources(pages_text: List[str], reference_sources: List[Dict[str, Any]], min_phrase_words: int = 4) -> Dict[str, Any]:
    """
    Compares document pages with sources.
    Matches sequences of 4+ consecutive words (Turnitin threshold).
    """
    total_doc_words = 0
    total_matched_words = 0
    
    processed_sources = []
    for idx, src in enumerate(reference_sources, start=1):
        color = TURNITIN_PALETTE[(idx - 1) % len(TURNITIN_PALETTE)]
        content = src.get("content", "")
        tokens = clean_tokens(content)
        processed_sources.append({
            "source_num": idx,
            "title": src.get("title", f"Sumber {idx}"),
            "source_name": src.get("source_name", "Internet / Jurnal Ilmiah"),
            "doi": src.get("doi", ""),
            "color": color,
            "tokens": tokens,
            "snippet": (content[:220].strip() + "...") if len(content) > 30 else src.get("title"),
            "matched_words": 0,
            "similarity_pct": 0.0
        })

    page_results = []
    for p_idx, page_raw in enumerate(pages_text):
        page_words = clean_tokens(page_raw)
        p_word_count = len(page_words)
        total_doc_words += p_word_count
        
        if p_word_count == 0:
            page_results.append({"page_index": p_idx, "matches": []})
            continue

        page_matches = []
        page_matched_w = set()

        for src in processed_sources:
            if not src["tokens"]:
                continue

            matcher = difflib.SequenceMatcher(None, page_words, src["tokens"], autojunk=False)
            blocks = matcher.get_matching_blocks()

            for b in blocks:
                if b.size >= min_phrase_words:
                    phrase_tokens = page_words[b.a : b.a + b.size]
                    phrase_text = " ".join(phrase_tokens)
                    
                    page_matches.append({
                        "source_num": src["source_num"],
                        "phrase": phrase_text,
                        "word_count": b.size
                    })
                    
                    for wi in range(b.a, b.a + b.size):
                        if wi not in page_matched_w:
                            page_matched_w.add(wi)
                            src["matched_words"] += 1
                            total_matched_words += 1

        page_results.append({
            "page_index": p_idx,
            "matches": page_matches
        })

    active_sources = []
    for src in processed_sources:
        if src["matched_words"] > 0 and total_doc_words > 0:
            src["similarity_pct"] = round((src["matched_words"] / total_doc_words) * 100, 1)
            active_sources.append(src)

    # Sort descending
    active_sources.sort(key=lambda x: x["similarity_pct"], reverse=True)
    overall_sim = round((total_matched_words / total_doc_words) * 100) if total_doc_words > 0 else 0

    return {
        "similarity_score": overall_sim,
        "total_words": total_doc_words,
        "matched_words": total_matched_words,
        "total_pages": len(pages_text),
        "sources": active_sources,
        "page_matches": page_results
    }
