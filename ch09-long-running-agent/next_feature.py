#!/usr/bin/env python3
"""Return the highest-priority incomplete feature from feature_list.json.

Called by the coding agent at the start of each session.
Outputs the first `passes: false` entry as JSON to stdout.
Returns an empty object `{}` when all features are complete.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) >= 2 else Path("feature_list.json")
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
    for feat in data:
        if isinstance(feat, dict) and not feat.get("passes", False):
            json.dump(feat, sys.stdout, ensure_ascii=False, indent=2)
            sys.stdout.write("\n")
            return 0
    sys.stdout.write("{}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
