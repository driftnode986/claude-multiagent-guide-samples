#!/bin/bash
# 書籍「Claude Code マルチエージェント実践ガイド」第2章
# ルーティング: タスクの種類に応じてモデルを使い分け
TASK_TYPE=$(claude -p "以下のタスクを分類してください: \
  簡単な質問/コード変更/アーキテクチャ設計 \
  タスク: $USER_QUERY" \
  --output-format json | jq -r '.classification')

case $TASK_TYPE in
  "簡単な質問")
    # 軽量モデルで高速応答
    claude -p "$USER_QUERY" --model haiku
    ;;
  "コード変更")
    # 標準モデルで実装
    claude -p "$USER_QUERY" --model sonnet
    ;;
  "アーキテクチャ設計")
    # 最高性能モデルで分析
    claude -p "$USER_QUERY" --model opus
    ;;
esac
