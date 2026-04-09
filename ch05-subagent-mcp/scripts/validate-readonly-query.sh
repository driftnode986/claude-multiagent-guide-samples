#!/bin/bash
# 書籍「Claude Code マルチエージェント実践ガイド」第5章
# ./scripts/validate-readonly-query.sh

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# 書き込み系SQLをブロック（大文字小文字を区別しない）
if echo "$COMMAND" | grep -iE '\b(INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE)\b' > /dev/null; then
  echo "Blocked: SELECT文のみ実行可能です"
  exit 2  # exit 2 = ツール実行をブロック
fi

exit 0
