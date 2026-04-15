#!/bin/bash
# Multi-Agent Development with Claude Code — Chapter 12
# Check lint and tests on task completion

if ! npm run lint --silent 2>/dev/null; then
  echo "Lint errors found. Fix them before completing the task."
  exit 2
fi

if ! npm test --silent 2>/dev/null; then
  echo "Tests are failing. Fix them before completing the task."
  exit 2
fi

exit 0
