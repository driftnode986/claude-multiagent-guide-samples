#!/bin/bash
# 書籍「Claude Code マルチエージェント実践ガイド」第2章
# 評価・最適化ループ: コード品質の反復改善
MAX_ITERATIONS=3
ITERATION=0

while [ $ITERATION -lt $MAX_ITERATIONS ]; do
  # 生成/改善
  if [ $ITERATION -eq 0 ]; then
    claude -p "src/api/handler.tsを \
      パフォーマンス最適化してください" \
      --output-format json > current.json
  else
    claude -p "前回のフィードバックに基づいて \
      src/api/handler.tsをさらに改善してください: \
      $(cat feedback.json)" \
      --output-format json > current.json
  fi

  # 評価
  claude -p "src/api/handler.tsの現在の状態を評価し、
    以下の基準でスコアを付けてください:
    - レスポンスタイム（1-10）
    - メモリ使用量（1-10）
    - コード可読性（1-10）
    合格基準: 全項目7以上" \
    --output-format json > feedback.json

  # 合格判定
  PASS=$(cat feedback.json | jq '.all_passed')
  if [ "$PASS" = "true" ]; then
    echo "評価合格: イテレーション $ITERATION で完了"
    break
  fi

  ITERATION=$((ITERATION + 1))
done
