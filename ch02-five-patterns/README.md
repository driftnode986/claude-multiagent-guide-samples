# Ch02: 5つのパターン＋動くサンプル

書籍「Claude Code マルチエージェント実践ガイド」第2章のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `prompt-chain.sh` | Shell | プロンプトチェーンパターン: ゲート付き逐次実行 |
| `routing.sh` | Shell | ルーティングパターン: タスク分類によるモデル使い分け |
| `parallel-review.sh` | Shell | 並列化パターン: コードレビューを3観点で並列実行 |
| `eval-optimize-loop.sh` | Shell | 評価・最適化パターン: 反復改善ループ |

## 使い方

各スクリプトは独立して実行できます。プロジェクトのルートディレクトリで実行してください。

```bash
# プロンプトチェーン（型チェック→テスト追加）
bash prompt-chain.sh

# ルーティング（USER_QUERY変数を設定して実行）
USER_QUERY="認証の仕組みを教えて" bash routing.sh

# 並列レビュー（mainブランチとの差分をレビュー）
bash parallel-review.sh

# 評価・最適化ループ（最大3回の改善サイクル）
bash eval-optimize-loop.sh
```

## 前提条件

- Claude Code CLI（最新版）
- Node.js / npm（prompt-chain.sh で `npx tsc` と `npm test` を使用）
- jq（routing.sh, eval-optimize-loop.sh で JSON パース）
- Git（parallel-review.sh で `git diff` を使用）
