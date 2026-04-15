# 第4章: カスタムサブエージェントの構築

「Claude Codeマルチエージェント実践ガイド」第4章のサンプルコードです。

## ファイル

| ファイル | 種別 | 説明 |
|---------|------|------|
| `agents/code-reviewer.md` | サブエージェント定義 | 基本的なコードレビューエージェント |
| `agents/test-writer.md` | サブエージェント定義 | 自動テスト生成エージェント |
| `agents/security-auditor.md` | サブエージェント定義 | OWASPトップ10に基づくセキュリティ監査エージェント |
| `agents/project-expert.md` | サブエージェント定義 | 永続メモリを持つプロジェクト知識エージェント |
| `scripts/validate-readonly-query.sh` | シェル | PreToolUseフック: SQLの書き込み操作をブロックする |

## 使い方

### サブエージェント定義のインストール

`agents/` 内のファイルをプロジェクトの `.claude/agents/` ディレクトリにコピーします。

```bash
mkdir -p .claude/agents
cp agents/*.md .claude/agents/
```

Claude Codeはタスクの文脈に基づいてサブエージェントを自動的に検出・選択します。

### バリデーションスクリプトのインストール

`scripts/validate-readonly-query.sh` は `db-reader` サブエージェントのPreToolUseフックとして使用します。

```bash
mkdir -p scripts
cp scripts/validate-readonly-query.sh scripts/
chmod +x scripts/validate-readonly-query.sh
```

## 動作要件

- Claude Code CLI（最新版）
- jq（バリデーションスクリプトが使用）
