#!/usr/bin/env python3
"""cost_alert.py — Multi-agent execution cost threshold monitor.

Read a JSONL log and alert (non-zero exit) if cumulative USD cost
or per-session max turns exceeds the configured threshold.

Usage:
    python cost_alert.py --log cost-log.jsonl --max-usd 10 --max-turns 50

Expected JSONL line format:
    {"session": "s1", "turn": 1, "model": "sonnet",
     "input_tokens": 1200, "output_tokens": 340}
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Reference prices for Anthropic Standard tier (USD per 1M tokens).
# These are illustrative values. Before production use, verify the
# latest prices at https://www.anthropic.com/pricing.
PRICING: dict[str, dict[str, float]] = {
    "haiku":  {"in": 1.00, "out": 5.00},
    "sonnet": {"in": 3.00, "out": 15.00},
    "opus":   {"in": 15.00, "out": 75.00},
}


def _nonneg_int(value: object, field: str) -> int:
    """Validate as a non-negative integer. Raise ValueError on bad input."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"{field} must be int, got {type(value).__name__}")
    if value < 0:
        raise ValueError(f"{field} must be >= 0, got {value}")
    return value


def usd_for(model: str, input_tokens: int, output_tokens: int) -> float:
    """Return the USD cost for one event. Raise ValueError for unknown models."""
    price = PRICING.get(model)
    if price is None:
        raise ValueError(f"unknown model: {model}")
    return (input_tokens * price["in"] + output_tokens * price["out"]) / 1_000_000


def aggregate(log_path: Path) -> dict:
    """Stream-aggregate the log file one line at a time."""
    total_usd = 0.0
    turns_by_session: dict[str, int] = {}
    with log_path.open("r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line:
                continue
            event = json.loads(line)
            in_tok = _nonneg_int(event["input_tokens"], "input_tokens")
            out_tok = _nonneg_int(event["output_tokens"], "output_tokens")
            total_usd += usd_for(event["model"], in_tok, out_tok)
            sid = event.get("session", "default")
            turn = _nonneg_int(event.get("turn", 0), "turn")
            turns_by_session[sid] = max(turns_by_session.get(sid, 0), turn)
    return {
        "total_usd": total_usd,
        "max_turns": max(turns_by_session.values(), default=0),
        "sessions": len(turns_by_session),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--log", required=True, type=Path)
    parser.add_argument("--max-usd", type=float, default=10.0)
    parser.add_argument("--max-turns", type=int, default=50)
    args = parser.parse_args()

    if not args.log.exists():
        print(f"[OK] no log file: {args.log}", file=sys.stderr)
        return 0

    try:
        stats = aggregate(args.log)
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"[ERROR] failed to parse {args.log}: {exc}", file=sys.stderr)
        return 2
    summary = (
        f"sessions={stats['sessions']} "
        f"total=${stats['total_usd']:.2f} "
        f"max_turns={stats['max_turns']}"
    )

    breached: list[str] = []
    if stats["total_usd"] > args.max_usd:
        breached.append(f"USD>{args.max_usd:.2f}")
    if stats["max_turns"] > args.max_turns:
        breached.append(f"turns>{args.max_turns}")

    if breached:
        print(f"[ALERT] {', '.join(breached)} | {summary}", file=sys.stderr)
        return 1
    print(f"[OK] {summary}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
