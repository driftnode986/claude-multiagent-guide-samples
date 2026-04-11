#!/usr/bin/env python3
"""feature_list.json の指定 feature を passes:true に切替える。

引数:
    description: feature の description（完全一致）
    feature_list.json: パス（省略時はカレント）

一致が 0 件または複数件のときはエラー終了する。description を
ユニークに保つことで、エージェントが誤って別の feature を
完了扱いにする事故を防ぐ。
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
