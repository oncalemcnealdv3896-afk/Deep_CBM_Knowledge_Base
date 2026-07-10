"""Deduplication engine — compare candidates against master index."""

from __future__ import annotations

import csv
import json
import re
import string
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
INDEX_DIR = ROOT / "00_Master" / "index"

PUNCT_TRANSLATION = str.maketrans(
    "", "", string.punctuation + "，。、《》？?！!：:；;（）()【】[]""''\"·—–-_"
)


def normalize_doi(value: Any) -> str:
    text = str(value).strip().lower() if value else ""
    text = re.sub(r"^https?://(dx\.)?doi\.org/", "", text)
    text = re.sub(r"^doi\s*:\s*", "", text, flags=re.IGNORECASE)
    return text.strip()


def normalize_title(value: Any) -> str:
    text = str(value).strip().lower() if value else ""
    text = text.translate(PUNCT_TRANSLATION)
    return re.sub(r"\s+", " ", text).strip()


def load_master_index() -> list[dict[str, str]]:
    """Load records from the master index JSONL file."""
    jsonl = INDEX_DIR / "Deep_CBM_master_index.jsonl"
    if not jsonl.exists():
        raise FileNotFoundError(f"Master index not found: {jsonl}")
    records: list[dict[str, str]] = []
    with jsonl.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def get_master_state() -> tuple[int, str]:
    """Return (count, last_dcbm_id) from master index."""
    records = load_master_index()
    if not records:
        return 0, ""
    ids: list[int] = []
    for r in records:
        m = re.search(r"DCBM[-_\s]?(\d+)", r.get("文献ID", ""), re.IGNORECASE)
        if m:
            ids.append(int(m.group(1)))
    if not ids:
        return len(records), ""
    last = sorted(ids)[-1]
    return len(records), f"DCBM-{last:03d}"


def deduplicate(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    """Run deduplication and return classification + logs.

    Returns dict with keys:
        results: list of (candidate, classification, details)
        new_count, duplicate_count, manual_review_count
        duplicate_log, manual_review_log
        proposed_final_ids
    """
    master = load_master_index()
    master_dois = {r.get("DOI_normalized", "") for r in master if r.get("DOI_normalized")}
    master_titles_en = {r.get("英文题名_normalized", "") for r in master if r.get("英文题名_normalized")}
    master_titles_zh = {r.get("中文题名_normalized", "") for r in master if r.get("中文题名_normalized")}

    results: list[dict[str, Any]] = []
    duplicate_log: list[dict[str, Any]] = []
    manual_review_log: list[dict[str, Any]] = []
    new_candidates: list[dict[str, Any]] = []

    for cand in candidates:
        doi_norm = normalize_doi(cand.get("doi", ""))
        title_en_norm = normalize_title(cand.get("title_en", ""))
        title_zh_norm = normalize_title(cand.get("title_zh", ""))
        first_author = str(cand.get("first_author", "")).strip().lower()
        year = str(cand.get("year", "")).strip()

        classification = "new"
        details: dict[str, Any] = {}

        # Level 1: DOI exact match
        if doi_norm and doi_norm in master_dois:
            existing = _find_by_doi(master, doi_norm)
            classification = "duplicate"
            details = {
                "duplicate_reason": "DOI exact match",
                "matched_field": "DOI_normalized",
                "existing_dcbm_id": existing.get("文献ID", "?"),
                "existing_doi": existing.get("DOI", ""),
                "existing_title": existing.get("英文题名", ""),
            }
            duplicate_log.append({"provisional_id": cand.get("provisional_id"), **details})
            results.append({"candidate": cand, "classification": classification, "details": details})
            continue

        # Level 2: English title normalized match
        if title_en_norm and title_en_norm in master_titles_en:
            existing = _find_by_title_en(master, title_en_norm)
            classification = "duplicate"
            details = {
                "duplicate_reason": "English title exact match",
                "matched_field": "英文题名_normalized",
                "existing_dcbm_id": existing.get("文献ID", "?"),
                "existing_doi": existing.get("DOI", ""),
                "existing_title": existing.get("英文题名", ""),
            }
            duplicate_log.append({"provisional_id": cand.get("provisional_id"), **details})
            results.append({"candidate": cand, "classification": classification, "details": details})
            continue

        # Level 3: Chinese title normalized match
        if title_zh_norm and title_zh_norm in master_titles_zh:
            existing = _find_by_title_zh(master, title_zh_norm)
            classification = "duplicate"
            details = {
                "duplicate_reason": "Chinese title exact match",
                "matched_field": "中文题名_normalized",
                "existing_dcbm_id": existing.get("文献ID", "?"),
                "existing_doi": existing.get("DOI", ""),
                "existing_title": existing.get("中文题名", ""),
            }
            duplicate_log.append({"provisional_id": cand.get("provisional_id"), **details})
            results.append({"candidate": cand, "classification": classification, "details": details})
            continue

        # Level 4: First author + year + high title similarity
        if first_author and year:
            similar = _find_similar(master, first_author, year, title_en_norm)
            if similar:
                similarity = similar.get("similarity", 0)
                if similarity >= 0.85:
                    classification = "duplicate"
                    details = {
                        "duplicate_reason": f"Author+Year+Title similarity ({similarity:.0%})",
                        "matched_field": "author_year_title",
                        "existing_dcbm_id": similar.get("文献ID", "?"),
                        "existing_doi": similar.get("DOI", ""),
                        "existing_title": similar.get("英文题名", ""),
                    }
                    duplicate_log.append({"provisional_id": cand.get("provisional_id"), **details})
                else:
                    classification = "manual_review"
                    details = {
                        "reason": f"Author+Year match, title similarity {similarity:.0%} < 85%",
                        "existing_dcbm_id": similar.get("文献ID", "?"),
                        "similarity": similarity,
                    }
                    manual_review_log.append({"provisional_id": cand.get("provisional_id"), **details})
                results.append({"candidate": cand, "classification": classification, "details": details})
                continue

        # Passed all checks → new
        new_candidates.append(cand)
        results.append({"candidate": cand, "classification": "new", "details": {}})

    # Assign proposed final IDs
    _, last_id = get_master_state()
    last_num = int(re.search(r"DCBM[-_\s]?(\d+)", last_id, re.IGNORECASE).group(1)) if last_id else 0
    proposed_ids: list[str] = []
    for i, _ in enumerate(new_candidates):
        proposed_ids.append(f"DCBM-{last_num + 1 + i:03d}")

    return {
        "results": results,
        "new_count": len(new_candidates),
        "duplicate_count": len(duplicate_log),
        "manual_review_count": len(manual_review_log),
        "duplicate_log": duplicate_log,
        "manual_review_log": manual_review_log,
        "proposed_final_ids": proposed_ids,
    }


def _find_by_doi(master: list[dict[str, str]], doi_norm: str) -> dict[str, str]:
    for r in master:
        if r.get("DOI_normalized", "") == doi_norm:
            return r
    return {}


def _find_by_title_en(master: list[dict[str, str]], title_norm: str) -> dict[str, str]:
    for r in master:
        if r.get("英文题名_normalized", "") == title_norm:
            return r
    return {}


def _find_by_title_zh(master: list[dict[str, str]], title_norm: str) -> dict[str, str]:
    for r in master:
        if r.get("中文题名_normalized", "") == title_norm:
            return r
    return {}


def _find_similar(
    master: list[dict[str, str]], author: str, year: str, title_norm: str
) -> dict[str, Any] | None:
    """Find records matching first-author + year, then check title similarity."""
    candidates = [
        r
        for r in master
        if r.get("第一作者", "").strip().lower() == author
        and r.get("年份", "").strip() == year
    ]
    best: tuple[float, dict[str, str]] = (0.0, {})
    for r in candidates:
        existing_title = r.get("英文题名_normalized", "")
        if existing_title and title_norm:
            sim = SequenceMatcher(None, title_norm, existing_title).ratio()
            if sim > best[0]:
                best = (sim, r)
    if best[0] > 0:
        result = dict(best[1])
        result["similarity"] = best[0]
        return result
    return None
