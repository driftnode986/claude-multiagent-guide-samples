#!/bin/bash
# Multi-Agent Development with Claude Code -- Chapter 1
# Run each agent in an infinite loop inside a Docker container
while true; do
    COMMIT=$(git rev-parse --short=6 HEAD)
    LOGFILE="agent_logs/agent_${COMMIT}.log"

    # Agent autonomously selects and executes tasks
    claude --dangerously-skip-permissions \
           -p "$(cat AGENT_PROMPT.md)" \
           --model claude-opus-X-Y &> "$LOGFILE"
done
