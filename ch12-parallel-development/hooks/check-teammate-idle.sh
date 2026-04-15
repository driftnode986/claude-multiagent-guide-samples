#!/bin/bash
# Multi-Agent Development with Claude Code — Chapter 12
# Run tests when a teammate goes idle

cd "$PROJECT_DIR"
if ! npm test --silent 2>/dev/null; then
  echo "Tests are failing. Fix them before marking the task complete."
  exit 2  # Exit code 2: send feedback and keep the teammate working
fi
exit 0
