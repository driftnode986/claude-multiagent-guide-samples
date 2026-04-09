# Ch04: カスタムサブエージェント作成

書籍「Claude Code マルチエージェント実践ガイド」第4章のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `agents/code-reviewer.md` | サブエージェント定義 | 基本的なコードレビューエージェント |
| `agents/test-writer.md` | サブエージェント定義 | テスト自動生成エージェント |
| `agents/security-auditor.md` | サブエージェント定義 | OWASP Top 10対応セキュリティ監査エージェント |
| `agents/project-expert.md` | サブエージェント定義 | 永続メモリ付きプロジェクト知識エージェント |
| `scripts/validate-readonly-query.sh` | Shell | PreToolUseフック: SQL書き込み操作をブロックするバリデーション |

## 使い方

### サブエージェント定義ファイルの配置

`agents/` 内のファイルをプロジェクトの `.claude/agents/` にコピーしてください。

```bash
mkdir -p .claude/agents
cp agents/*.md .claude/agents/
```

Claude Codeが自動的にサブエージェントを認識し、タスクに応じて選択します。

### バリデーションスクリプトの配置

`scripts/validate-readonly-query.sh` は `db-reader` サブエージェントのPreToolUseフックとして使用します。

```bash
mkdir -p scripts
cp scripts/validate-readonly-query.sh scripts/
chmod +x scripts/validate-readonly-query.sh
```

## 前提条件

- Claude Code CLI（最新版）
- jq（バリデーションスクリプトで使用）
