# Ch14: Production Reliability

Sample code and reference material for Chapter 14 of *Multi-Agent Development with Claude Code*.

## Overview

This chapter focuses on operational patterns and checklists. The companion code provides a minimal implementation of cost threshold alerting -- the topic most amenable to concrete code.

## Files

| File | Description |
|------|-------------|
| `cost_alert.py` | Aggregates JSONL logs and detects cumulative cost or max-turn threshold breaches |
| `record_turn.sh` | Shell helper that appends one turn event to `cost-log.jsonl` |
| `sample-events.jsonl` | Sample log for testing (4 events across 2 sessions) |

## Quick Start

```bash
# Run threshold check against the sample log (10 USD / 50 turns)
python cost_alert.py --log sample-events.jsonl --max-usd 10 --max-turns 50

# Expected output (stderr)
# [OK] sessions=2 total=$0.57 max_turns=3
```

To simulate a threshold breach:

```bash
# Use a low threshold to trigger the alert
python cost_alert.py --log sample-events.jsonl --max-usd 0.1 --max-turns 50
# [ALERT] USD>0.10 | sessions=2 total=$0.57 max_turns=3
# (exit 1)
```

Invalid model names or malformed JSON produce exit code 2 with `[ERROR]`, distinct from the alert exit code, to catch logging bugs early.

To append new turn events, use `record_turn.sh`:

```bash
# usage: ./record_turn.sh <session> <turn> <model> <in_tokens> <out_tokens>
COST_LOG=cost-log.jsonl ./record_turn.sh s1 1 sonnet 1200 340
COST_LOG=cost-log.jsonl ./record_turn.sh s1 2 opus 15000 4200
python cost_alert.py --log cost-log.jsonl --max-usd 10 --max-turns 50
```

## Integrating with a Harness

Call `record_turn.sh` after each tool call in the harness from Chapter 9 (or any custom script). At the end of each session, run `cost_alert.py` and halt new sessions if the exit code is non-zero.

```bash
# Example session-end hook
if ! python cost_alert.py --log cost-log.jsonl --max-usd 10 --max-turns 50; then
  echo "Cost threshold exceeded. Investigate before continuing."
  exit 1
fi
```

## Pricing Table Maintenance

The `PRICING` dictionary at the top of `cost_alert.py` contains reference prices for Anthropic's Standard tier (for illustration only). Before production use, verify the latest prices at https://www.anthropic.com/pricing and update the dictionary. When new models or pricing changes arrive, only this one dictionary needs updating.

## Key Topics (Book Text)

| Topic | Content |
|-------|---------|
| Checkpoint strategy | Recovery design through periodic and error-triggered checkpoints |
| Trace log structure | Per-session step recording (tool calls, tokens, duration) |
| Model tiering | Cost-optimal placement: lead (Opus), worker (Sonnet), validator (Haiku) |
| Permission hierarchy | Permission design for development, CI/CD, and production environments |
| Rainbow deployments | Running multiple versions simultaneously with gradual traffic shifting |
| Incident response | Detection and response flows for infinite loops, cost runaway, quality degradation, and cascade failures |

## References

- Anthropic Engineering Blog, "How we built our multi-agent research system" (2025-06)
- Anthropic Engineering Blog, "Building a C compiler with a team of parallel Claudes" (2026-02)
- Anthropic pricing page: https://www.anthropic.com/pricing

## Prerequisites

- Python 3.9 or later
- Bash 4 or later (for `record_turn.sh`)
- Claude Code CLI (latest version)
