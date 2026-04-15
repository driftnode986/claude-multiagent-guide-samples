#!/usr/bin/env bash
# record_turn.sh — Append one turn's cost event to cost-log.jsonl.
# Usage: ./record_turn.sh <session> <turn> <model> <in_tokens> <out_tokens>
#
# Override the log file path with the COST_LOG environment variable.
set -euo pipefail

if [ "$#" -ne 5 ]; then
  echo "usage: $0 <session> <turn> <model> <in_tokens> <out_tokens>" >&2
  exit 2
fi

# Reject characters that could break JSONL parsing (quotes, newlines, etc.)
case "$1" in *[!A-Za-z0-9._-]*|"") echo "invalid session: $1" >&2; exit 2;; esac
case "$3" in *[!A-Za-z0-9._-]*|"") echo "invalid model: $3"   >&2; exit 2;; esac

# Require non-negative integers for turn and token counts
for n in "$2" "$4" "$5"; do
  case "$n" in ''|*[!0-9]*) echo "non-negative integer required: $n" >&2; exit 2;; esac
done

LOG="${COST_LOG:-cost-log.jsonl}"

# Append one validated line
printf '{"session":"%s","turn":%s,"model":"%s","input_tokens":%s,"output_tokens":%s}\n' \
  "$1" "$2" "$3" "$4" "$5" >> "$LOG"
