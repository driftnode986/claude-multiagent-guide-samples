# 第12章: エージェントチームの実践

「Claude Codeマルチエージェント実践ガイド」第12章のサンプルコードです。

## ファイル

| ファイル | 種別 | 説明 |
|---------|------|------|
| `claude-json-teammate-mode.json` | JSON | `~/.claude.json` 用のチームメンバー表示モード設定 |
| `settings-teammate-idle.json` | JSON | TeammateIdle フック用の `settings.json` 設定 |
| `hooks/check-teammate-idle.sh` | シェル | チームメンバーがアイドルになったときにテストを実行する品質ゲート |
| `hooks/check-task-completed.sh` | シェル | タスク完了時にリントとテストをチェックする品質ゲート |

## 使い方

### 表示モードの設定

`claude-json-teammate-mode.json` の内容を `~/.claude.json` にマージします。オプションは `"auto"`（デフォルト）、`"in-process"`、`"split-pane"` のいずれかです。

### フックによる品質ゲートの設定

1. `settings-teammate-idle.json` をプロジェクトの `.claude/settings.json` にマージする
2. `hooks/` 以下のスクリプトを `.claude/hooks/` にコピーする
3. 実行権限を付与する: `chmod +x .claude/hooks/*.sh`

フックは終了コード `2` を返すことで、チームメンバーにフィードバックを送り作業継続を指示します。

## 動作要件

- Claude Code CLI（最新版）
- `npm test` / `npm run lint` が動作するNode.jsプロジェクト
