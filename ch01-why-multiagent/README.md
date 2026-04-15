# 第1章: マルチエージェントが必要な理由

「Claude Codeマルチエージェント実践ガイド」第1章のサンプルコードです。

## ファイル

| ファイル | 種別 | 説明 |
|---------|------|------|
| `agent-harness.sh` | シェル | CコンパイラプロジェクトのAgentハーネス（無限ループ実行） |
| `AGENT_PROMPT.md` | Markdown | エージェント指示プロンプト（`agent-harness.sh` が読み込む） |

## 使い方

`agent-harness.sh` は、AnthropicのCコンパイラプロジェクトで使われたハーネス構造を示します。各エージェントはDockerコンテナ内で無限ループとして動作し、タスクを自律的に選択・実行します。

```bash
# AGENT_PROMPT.md が同じディレクトリにあることを確認してから実行
bash agent-harness.sh
```

> **警告**: このスクリプトは `--dangerously-skip-permissions` を使用します。本番環境での実行には十分注意してください。

## 動作要件

- Claude Code CLI（最新版）
- Git
- Docker（本番環境で使用する場合）
