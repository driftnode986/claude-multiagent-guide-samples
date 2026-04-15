#!/bin/bash
# Multi-Agent Development with Claude Code -- Chapter 2
# Evaluator-optimizer loop: iterative code quality improvement
MAX_ITERATIONS=3
ITERATION=0

while [ $ITERATION -lt $MAX_ITERATIONS ]; do
  # Generate / improve
  if [ $ITERATION -eq 0 ]; then
    claude -p "Optimize src/api/handler.ts for performance" \
      --output-format json > current.json
  else
    claude -p "Improve src/api/handler.ts based on this feedback: \
      $(cat feedback.json)" \
      --output-format json > current.json
  fi

  # Evaluate
  claude -p "Evaluate the current state of src/api/handler.ts.
    Score each criterion from 1 to 10:
    - Response time
    - Memory usage
    - Code readability
    Pass threshold: all scores 7 or above" \
    --output-format json > feedback.json

  # Check pass/fail
  PASS=$(cat feedback.json | jq '.all_passed')
  if [ "$PASS" = "true" ]; then
    echo "Evaluation passed at iteration $ITERATION"
    break
  fi

  ITERATION=$((ITERATION + 1))
done
