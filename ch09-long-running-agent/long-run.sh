#!/bin/bash
# 書籍「Claude Code マルチエージェント実践ガイド」第9章
# long-run.sh — コンテナ内での実行を推奨

while true; do
    COMMIT=$(git rev-parse --short=6 HEAD)
    LOGFILE="agent_logs/agent_${COMMIT}.log"

    claude --agent project-worker \
           --dangerously-skip-permissions \
           -p "$(cat AGENT_PROMPT.md)" \
           --model claude-opus-4-6 &> "$LOGFILE"
done
