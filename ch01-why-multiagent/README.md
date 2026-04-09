# Ch01: なぜマルチエージェントか

書籍「Claude Code マルチエージェント実践ガイド」第1章のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `agent-harness.sh` | Shell | C Compilerプロジェクトで使われたエージェントハーネス（無限ループ実行） |
| `AGENT_PROMPT.md` | Markdown | エージェントへの指示書（`agent-harness.sh` が読み込む） |

## 使い方

`agent-harness.sh` はAnthropicのC Compilerプロジェクトで使われたエージェントハーネスの構造を示すサンプルです。各エージェントをDockerコンテナ内で無限ループ実行し、タスクを自律的に選択・実行します。

```bash
# 実行前に AGENT_PROMPT.md を用意してください
bash agent-harness.sh
```

> **注意**: このスクリプトは `--dangerously-skip-permissions` を使用します。本番環境での使用は十分に注意してください。

## 前提条件

- Claude Code CLI（最新版）
- Git
- Docker（本番利用時）
