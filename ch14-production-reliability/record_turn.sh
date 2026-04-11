#!/usr/bin/env bash
# record_turn.sh — 1ターン分のコストイベントを cost-log.jsonl に追記する。
# 使い方: ./record_turn.sh <session> <turn> <model> <in_tokens> <out_tokens>
#
# 環境変数 COST_LOG でログファイルパスを上書きできる。
set -euo pipefail

if [ "$#" -ne 5 ]; then
  echo "usage: $0 <session> <turn> <model> <in_tokens> <out_tokens>" >&2
  exit 2
fi

LOG="${COST_LOG:-cost-log.jsonl}"

# JSONL を整形して 1 行追記する。printf を使うことで shell escape を避ける。
printf '{"session":"%s","turn":%s,"model":"%s","input_tokens":%s,"output_tokens":%s}\n' \
  "$1" "$2" "$3" "$4" "$5" >> "$LOG"
