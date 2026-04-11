#!/usr/bin/env python3
"""features.txt から feature_list.json を生成する。

人間は features.txt を markdown 風に書き、このスクリプトが
JSON に変換する。再生成しても既存の `passes: true` は引き継がれる
ため、進捗を失わずに features.txt を編集できる。

features.txt の書式:

    # functional: ユーザーがログインできる
    - メールアドレスを入力する
    - パスワードを入力する
    - ログインボタンをクリックする

    # ui: サイドバーが折りたたまれる
    - 折りたたみボタンをクリックする
    - サイドバーが非表示になることを確認する

`# <category>: <description>` で feature が始まり、`-` で steps を
列挙する。空行は区切りとして無視される。
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

FEATURE_HEAD = re.compile(r"^#\s*([^:]+):\s*(.+)$")
STEP = re.compile(r"^-\s*(.+)$")


def parse_features(text: str) -> list[dict]:
    features: list[dict] = []
    current: dict | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line:
            continue
        head = FEATURE_HEAD.match(line)
        if head:
            if current is not None and current["steps"]:
                features.append(current)
            current = {
                "category": head.group(1).strip(),
                "description": head.group(2).strip(),
                "steps": [],
                "passes": False,
            }
            continue
        step = STEP.match(line)
        if step and current is not None:
            current["steps"].append(step.group(1).strip())
    if current is not None and current["steps"]:
        features.append(current)
    return features


def merge_passes(new: list[dict], existing_path: Path) -> list[dict]:
    if not existing_path.exists():
        return new
    try:
        existing = json.loads(existing_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return new
    if not isinstance(existing, list):
        return new
    by_desc = {
        f.get("description"): bool(f.get("passes"))
        for f in existing
        if isinstance(f, dict)
    }
    for feat in new:
        if by_desc.get(feat["description"], False):
            feat["passes"] = True
    return new


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(
            "usage: generate_features.py <features.txt> [feature_list.json]",
            file=sys.stderr,
        )
        return 2
    src = Path(argv[1])
    dst = Path(argv[2]) if len(argv) >= 3 else Path("feature_list.json")
    if not src.exists():
        print(f"error: {src} not found", file=sys.stderr)
        return 1
    features = parse_features(src.read_text(encoding="utf-8"))
    if not features:
        print(f"error: no features parsed from {src}", file=sys.stderr)
        return 1
    features = merge_passes(features, dst)
    dst.write_text(
        json.dumps(features, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    done = sum(1 for f in features if f["passes"])
    pending = len(features) - done
    print(
        f"wrote {dst}: {len(features)} features "
        f"({done} passed, {pending} pending)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
