#!/bin/bash
# init.sh — 初期化エージェントが生成する環境セットアップスクリプト
# 長期実行エージェントの各セッション開始時に実行される

set -euo pipefail

echo "=== 開発環境セットアップ ==="

# 依存関係のインストール
if [ -f "package.json" ]; then
    echo "Node.js依存関係をインストール中..."
    npm install
fi

if [ -f "requirements.txt" ]; then
    echo "Python依存関係をインストール中..."
    pip install -r requirements.txt
fi

# 開発サーバーの起動（バックグラウンド）
if [ -f "package.json" ]; then
    echo "開発サーバーを起動中..."
    npm run dev &
    DEV_PID=$!
    echo "開発サーバー PID: $DEV_PID"

    # サーバーの起動を待機
    sleep 3
    echo "開発サーバー起動完了"
fi

# テスト環境の確認
echo "=== テスト環境確認 ==="
if [ -f "package.json" ]; then
    npm test -- --passWithNoTests 2>/dev/null && echo "テスト環境: OK" || echo "テスト環境: 要確認"
fi

echo "=== セットアップ完了 ==="
