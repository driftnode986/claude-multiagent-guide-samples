# 第2章: 5つのワークフローパターン

「Claude Codeマルチエージェント実践ガイド」第2章のサンプルコードです。

## ファイル

| ファイル | 種別 | 説明 |
|---------|------|------|
| `prompt-chain.sh` | シェル | プロンプトチェーンパターン: ゲート付き逐次実行 |
| `routing.sh` | シェル | ルーティングパターン: タスク分類に基づくモデル選択 |
| `parallel-review.sh` | シェル | 並列化パターン: 3つの視点によるコードレビュー |
| `eval-optimize-loop.sh` | シェル | 評価者・最適化者パターン: 反復的な改善ループ |

## 使い方

各スクリプトは独立して実行できます。プロジェクトのルートディレクトリから実行してください。

```bash
# プロンプトチェーン（型チェック -> テスト追加）
bash prompt-chain.sh

# ルーティング（実行前に USER_QUERY 変数をセット）
USER_QUERY="認証の仕組みを説明してください" bash routing.sh

# 並列レビュー（main と HEAD の差分をレビューする）
bash parallel-review.sh

# 評価者・最適化者ループ（最大3回の改善サイクル）
bash eval-optimize-loop.sh
```

## 動作要件

- Claude Code CLI（最新版）
- Node.js / npm（`prompt-chain.sh` が `npx tsc` と `npm test` を使用）
- jq（`routing.sh`、`eval-optimize-loop.sh` がJSON解析に使用）
- Git（`parallel-review.sh` が `git diff` を使用）
