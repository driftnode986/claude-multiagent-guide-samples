# 付録A: クイックリファレンス

「Claude Codeマルチエージェント実践ガイド」付録Aのサンプルファイルです。

## ファイル

| ファイル | 種別 | 説明 |
|---------|------|------|
| `agent-definition-template.md` | サブエージェント定義 | YAMLフロントマター + Markdownボディのテンプレート |
| `agent-tool-params.json` | JSON | `Agent` ツールのパラメータリファレンス |
| `mcp-inline-template.yml` | YAML | インラインMCPサーバー定義テンプレート |

## 使い方

### サブエージェント定義の作成

`agent-definition-template.md` をプロジェクトの `.claude/agents/` にコピーします。`name`、`description`、`model`、`tools` フィールドを自分の値に書き換えてください。Markdownのボディ部分がサブエージェントのシステムプロンプトになります。

### Agent ツールのパラメータ

`agent-tool-params.json` はClaude Codeがサブエージェントを内部でスポーンする際に使用するパラメータ構造を示しています。最も重要なのは `prompt` フィールドで、サブエージェントへの詳細な指示が含まれます。

### MCPインライン定義

`mcp-inline-template.yml` はサブエージェント定義内でMCPサーバーをインラインで定義するためのテンプレートです。環境変数の参照には `${API_KEY}` 構文を使用します。

## 動作要件

- Claude Code CLI（最新版）
