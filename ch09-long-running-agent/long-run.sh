#!/bin/bash
# Multi-Agent Development with Claude Code -- Chapter 9
# long-run.sh -- recommended to run inside a container

while true; do
    COMMIT=$(git rev-parse --short=6 HEAD)
    LOGFILE="agent_logs/agent_${COMMIT}.log"

    claude --agent project-worker \
           --dangerously-skip-permissions \
           -p "$(cat AGENT_PROMPT.md)" \
           --model claude-opus-4-6 &> "$LOGFILE"
done
