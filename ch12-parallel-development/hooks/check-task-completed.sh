#!/bin/bash
# 書籍「Claude Code マルチエージェント実践ガイド」第12章
# タスク完了時にリントとテストを確認

if ! npm run lint --silent 2>/dev/null; then
  echo "リントエラーがあります。修正してからタスクを完了してください。"
  exit 2
fi

if ! npm test --silent 2>/dev/null; then
  echo "テストが失敗しています。修正してからタスクを完了してください。"
  exit 2
fi

exit 0
