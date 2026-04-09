# Appendix A: コマンド・設定リファレンス

書籍「Claude Code マルチエージェント実践ガイド」Appendix A のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `agent-definition-template.md` | サブエージェント定義 | YAMLフロントマター + Markdown本文のテンプレート |
| `agent-tool-params.json` | JSON | `Agent` ツールのパラメータリファレンス |
| `mcp-inline-template.yml` | YAML | MCPサーバーのインライン定義テンプレート |

## 使い方

### サブエージェント定義の作成

`agent-definition-template.md` をコピーして `.claude/agents/` に配置し、`name`、`description`、`model`、`tools` を書き換えてください。

### Agent ツールのパラメータ

`agent-tool-params.json` は Claude Code 内部でサブエージェントを起動する際のパラメータ構造です。`prompt` フィールドが最重要で、サブエージェントへの詳細な指示を記述します。

### MCP インライン定義

`mcp-inline-template.yml` はサブエージェント定義内でMCPサーバーをインライン定義する際のテンプレートです。`${API_KEY}` のような環境変数参照が使えます。

## 前提条件

- Claude Code CLI（最新版）
