---
name: eval-runner
description: Execute evaluation tasks and record results
model: sonnet
tools: Bash, Read, Write, Glob, Grep
---

An agent that executes evaluation tasks and records results.

Steps:
1. Read task definitions from the eval-tasks/ directory.
2. Execute each task and record pass/fail outcomes.
3. Save results to eval-results/.
4. Generate a summary report.
