#!/bin/bash
# 書籍「Claude Code マルチエージェント実践ガイド」第4章
# ./scripts/validate-readonly-query.sh

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# SQL書き込み操作をブロック（大文字小文字不問）
if echo "$COMMAND" | grep -iE \
  '\b(INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE)\b' \
  > /dev/null; then
  echo "Blocked: Only SELECT queries are allowed" >&2
  exit 2
fi

exit 0
