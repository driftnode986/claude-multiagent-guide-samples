#!/bin/bash
# Multi-Agent Development with Claude Code -- Chapter 2
# Step 1: Generate the code change
claude -p "Refactor the authentication logic in src/auth.ts to use JWT" \
  --output-format json > step1_result.json

# Gate: type check
npx tsc --noEmit
if [ $? -ne 0 ]; then
  echo "Type errors detected. Retrying step 1."
  exit 1
fi

# Step 2: Add tests for the change
claude -p "Add tests for the changes made to src/auth.ts" \
  --output-format json > step2_result.json

# Gate: run tests
npm test
