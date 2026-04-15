#!/usr/bin/env python3
"""Set passes to true for the specified feature in feature_list.json.

Args:
    description: The feature description (exact match)
    feature_list.json: Path (defaults to current directory)

Exits with an error if zero or multiple features match. Keeping
descriptions unique prevents the agent from accidentally marking
the wrong feature as complete.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(
            "usage: mark_passed.py <description> [feature_list.json]",
            file=sys.stderr,
        )
        return 2
    description = argv[1]
    path = Path(argv[2]) if len(argv) >= 3 else Path("feature_list.json")
    if not path.exists():
        print(f"error: {path} not found", file=sys.stderr)
        return 1
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"error: invalid JSON in {path}: {exc}", file=sys.stderr)
        return 1
    if not isinstance(data, list):
        print(
            "error: feature_list.json must be a JSON array",
            file=sys.stderr,
        )
        return 1
    matches = [
        f
        for f in data
        if isinstance(f, dict) and f.get("description") == description
    ]
    if len(matches) == 0:
        print(
            f"error: no feature matched description: {description}",
            file=sys.stderr,
        )
        return 1
    if len(matches) > 1:
        print(
            f"error: multiple features matched description: {description}",
            file=sys.stderr,
        )
        return 1
    matches[0]["passes"] = True
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"marked passed: {description}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
