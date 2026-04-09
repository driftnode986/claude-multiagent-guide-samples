#!/bin/bash
# 書籍「Claude Code マルチエージェント実践ガイド」第2章
# ステップ1: コード変更の生成
claude -p "src/auth.tsの認証ロジックをJWT方式に変更してください" \
  --output-format json > step1_result.json

# ゲート: 型チェック
npx tsc --noEmit
if [ $? -ne 0 ]; then
  echo "型エラーが発生。ステップ1をやり直します"
  exit 1
fi

# ステップ2: テストの追加
claude -p "src/auth.tsの変更に対するテストを追加してください" \
  --output-format json > step2_result.json

# ゲート: テスト実行
npm test
