# Ch05: サブエージェント + MCP連携

書籍「Claude Code マルチエージェント実践ガイド」第5章のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `agents/web-scraper.md` | サブエージェント定義 | Playwright MCPを使ったWebスクレイピングエージェント |
| `agents/pr-reviewer.md` | サブエージェント定義 | GitHub MCPを使ったPRコードレビューエージェント |
| `agents/deployment-checker.md` | サブエージェント定義 | Playwright + Datadog MCPを使ったデプロイ後の動作確認エージェント |
| `scripts/validate-readonly-query.sh` | シェルスクリプト | SQL書き込みをブロックするPreToolUseフックスクリプト |

## 使い方

### サブエージェント定義の配置

`.md`ファイルをプロジェクトの`.claude/agents/`ディレクトリにコピーしてください。

```bash
cp agents/*.md your-project/.claude/agents/
```

### バリデーションスクリプトの配置

```bash
cp scripts/validate-readonly-query.sh your-project/scripts/
chmod +x your-project/scripts/validate-readonly-query.sh
```

### サブエージェントの呼び出し

Claude Codeのメインセッションで自然言語で指示するだけで、適切なサブエージェントが自動選択されます。

```
あなた: https://example.com/products のページから全商品の名前と価格を収集して
あなた: PR #42 をレビューして
```

## 前提条件

- Claude Code CLI（最新版）
- Node.js（npxでMCPサーバーを起動するため）
- GitHub MCP利用時: GitHubの認証設定
- バリデーションスクリプト利用時: jq コマンド
