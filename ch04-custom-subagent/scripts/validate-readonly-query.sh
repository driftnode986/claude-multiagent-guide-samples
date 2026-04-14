#!/bin/bash
# Ch04 - Multi-Agent Development with Claude Code
# PreToolUse hook: block SQL write operations

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Block SQL write operations (case-insensitive)
if echo "$COMMAND" | grep -iE \
  '\b(INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE)\b' \
  > /dev/null; then
  echo "Blocked: Only SELECT queries are allowed"
  exit 2
fi

exit 0
