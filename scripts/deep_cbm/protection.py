"""Protection checks — verify protected directories are not modified."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

PROTECTED_DIRS = [
    "08_User",
    "00_Master/source",
    "00_Master/workbook_archive",
    "00_Master/snapshots",
]


def hash_protected_paths() -> dict[str, str]:
    """Return a hash dict for all files under protected directories."""
    result: dict[str, str] = {}
    for rel_dir in PROTECTED_DIRS:
        full = ROOT / rel_dir
        if not full.exists():
            continue
        for fp in sorted(full.rglob("*")):
            if fp.is_file():
                rel = fp.relative_to(ROOT).as_posix()
                result[rel] = _sha256(fp)
    return result


def save_protected_snapshot(path: Path) -> dict[str, str]:
    """Save hash snapshot to a JSON file, return the hash dict."""
    hashes = hash_protected_paths()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(hashes, ensure_ascii=False, indent=2), encoding="utf-8")
    return hashes


def verify_protected_paths(before_path: Path) -> dict[str, Any]:
    """Compare current protected paths against a saved snapshot."""
    if not before_path.exists():
        return {"modified": False, "error": "before snapshot not found", "changes": []}

    before: dict[str, str] = json.loads(before_path.read_text(encoding="utf-8"))
    after = hash_protected_paths()

    changes = []
    all_keys = set(before.keys()) | set(after.keys())
    for key in sorted(all_keys):
        if key not in before:
            changes.append({"path": key, "change": "added"})
        elif key not in after:
            changes.append({"path": key, "change": "removed"})
        elif before[key] != after[key]:
            changes.append({"path": key, "change": "modified"})

    return {
        "modified": len(changes) > 0,
        "before_count": len(before),
        "after_count": len(after),
        "changes": changes,
    }


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()
