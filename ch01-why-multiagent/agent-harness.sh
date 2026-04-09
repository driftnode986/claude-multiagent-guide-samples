#!/bin/bash
# 書籍「Claude Code マルチエージェント実践ガイド」第1章
# 各エージェントをDockerコンテナ内で無限ループ実行
while true; do
    COMMIT=$(git rev-parse --short=6 HEAD)
    LOGFILE="agent_logs/agent_${COMMIT}.log"

    # エージェントがタスクを自律的に選択・実行
    claude --dangerously-skip-permissions \
           -p "$(cat AGENT_PROMPT.md)" \
           --model claude-opus-X-Y &> "$LOGFILE"
done
