# 第5章: MCPでサブエージェントを外部ツールと接続する

「Claude Codeマルチエージェント実践ガイド」第5章のサンプルコードです。

## ファイル

| ファイル | 種別 | 説明 |
|---------|------|------|
| `agents/web-scraper.md` | サブエージェント定義 | Playwright MCPを使ったWebスクレイピングエージェント |
| `agents/pr-reviewer.md` | サブエージェント定義 | GitHub MCPを使ったPRコードレビューエージェント |
| `agents/deployment-checker.md` | サブエージェント定義 | Playwright + Datadog MCPを使ったデプロイ後検証エージェント |
| `scripts/validate-readonly-query.sh` | シェルスクリプト | SQLの書き込み操作をブロックするPreToolUseフック |

## 使い方

### サブエージェント定義の配置

`.md` ファイルをプロジェクトの `.claude/agents/` ディレクトリにコピーします。

```bash
cp agents/*.md your-project/.claude/agents/
```

### バリデーションスクリプトの配置

```bash
cp scripts/validate-readonly-query.sh your-project/scripts/
chmod +x your-project/scripts/validate-readonly-query.sh
```

### サブエージェントの呼び出し

メインセッションから自然言語でタスクを指示すると、Claude Codeが適切なサブエージェントを自動的に選択します。

```
あなた: https://example.com/products から全商品名と価格をスクレイピングしてください
あなた: PR #42 をレビューしてください
```

## 動作要件

- Claude Code CLI（最新版）
- Node.js（npx 経由でMCPサーバーを起動するために必要）
- GitHub MCP: GitHubの認証設定が必要
- バリデーションスクリプト: jq のインストールが必要
