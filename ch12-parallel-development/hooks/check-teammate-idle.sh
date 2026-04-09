#!/bin/bash
# 書籍「Claude Code マルチエージェント実践ガイド」第12章
# チームメイトのアイドル時にテストを実行

cd "$PROJECT_DIR"
if ! npm test --silent 2>/dev/null; then
  echo "テストが失敗しています。修正してから完了してください。"
  exit 2  # 終了コード2: フィードバックを送信して作業を継続させる
fi
exit 0
