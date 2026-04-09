# Ch12: 実践・並列開発

書籍「Claude Code マルチエージェント実践ガイド」第12章のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `claude-json-teammate-mode.json` | JSON | `~/.claude.json` に配置するチームメイト表示モード設定 |
| `settings-teammate-idle.json` | JSON | TeammateIdle Hooks の `settings.json` 設定 |
| `hooks/check-teammate-idle.sh` | Shell | チームメイトのアイドル時にテストを実行する品質ゲート |
| `hooks/check-task-completed.sh` | Shell | タスク完了時にリントとテストを確認する品質ゲート |

## 使い方

### 表示モードの設定

`claude-json-teammate-mode.json` の内容を `~/.claude.json` にマージしてください。選択肢は `"auto"`（デフォルト）、`"in-process"`、`"split-pane"` です。

### Hooks による品質ゲート

1. `settings-teammate-idle.json` の内容をプロジェクトの `.claude/settings.json` にマージ
2. `hooks/` 配下のスクリプトを `.claude/hooks/` にコピー
3. 実行権限を付与: `chmod +x .claude/hooks/*.sh`

Hooks は終了コード `2` でフィードバックを返し、チームメイトに作業の継続を指示します。

## 前提条件

- Claude Code CLI（最新版）
- Node.js プロジェクト（`npm test` / `npm run lint` が動作すること）
