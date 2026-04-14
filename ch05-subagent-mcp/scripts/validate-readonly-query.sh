#!/bin/bash
# "Multi-Agent Development with Claude Code" - Chapter 5
# ./scripts/validate-readonly-query.sh
# PreToolUse hook: blocks write SQL statements

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Block write SQL statements (case-insensitive)
if echo "$COMMAND" | grep -iE '\b(INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE)\b' > /dev/null; then
  echo "Blocked: only SELECT queries are allowed"
  exit 2  # exit 2 = block tool execution
fi

exit 0
