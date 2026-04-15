#!/bin/bash
# Multi-Agent Development with Claude Code -- Chapter 2
# Parallelization: review code from three perspectives simultaneously
claude -p "Review the following PR from three perspectives at once:
1. Security vulnerabilities
2. Performance issues
3. Coding convention violations

Delegate each perspective to a subagent and run them in parallel.
Target: $(git diff main...HEAD)"
