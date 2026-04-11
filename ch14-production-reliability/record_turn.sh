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

# session/model に JSON エスケープが必要な文字を許さない。
# 引用符・改行・制御文字の混入で後段の JSONL パースが壊れることを防ぐ。
case "$1" in *[!A-Za-z0-9._-]*|"") echo "invalid session: $1" >&2; exit 2;; esac
case "$3" in *[!A-Za-z0-9._-]*|"") echo "invalid model: $3"   >&2; exit 2;; esac

# turn / tokens は非負整数のみ受け付ける。
for n in "$2" "$4" "$5"; do
  case "$n" in ''|*[!0-9]*) echo "non-negative integer required: $n" >&2; exit 2;; esac
done

LOG="${COST_LOG:-cost-log.jsonl}"

# 入力検証済みの値だけを使って 1 行追記する。
printf '{"session":"%s","turn":%s,"model":"%s","input_tokens":%s,"output_tokens":%s}\n' \
  "$1" "$2" "$3" "$4" "$5" >> "$LOG"
