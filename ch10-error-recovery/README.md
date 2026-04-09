# Ch10: エラー回復と失敗モード分類

書籍「Claude Code マルチエージェント実践ガイド」第10章のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `recovery-strategies.yml` | YAML | 4カテゴリの失敗モードとリカバリー戦略 |
| `agents/risky-refactor.md` | サブエージェント | worktree分離でリスクの高いリファクタリングを実行 |
| `agents/resilient-worker.md` | サブエージェント | エラーに強い作業エージェント（Hooks付き） |
| `agents/careful-worker.md` | サブエージェント | 不確実な場合に停止するhuman-in-the-loopエージェント |
| `graceful-degradation.yml` | YAML | グレースフルデグレードの4段階レベル定義 |
| `CLAUDE-degrade-rules.md` | CLAUDE.mdテンプレート | グレースフルデグレードルール |
| `failure-log-template.md` | テンプレート | 失敗記録のログテンプレート |
| `agent-memory-template.md` | テンプレート | サブエージェント永続メモリ用MEMORY.mdテンプレート |

## 使い方

```bash
# サブエージェント定義を配置
cp agents/*.md .claude/agents/

# グレースフルデグレードルールをCLAUDE.mdに追記
cat CLAUDE-degrade-rules.md >> CLAUDE.md

# 失敗記録テンプレートを使ってログを管理
cp failure-log-template.md docs/failure-log.md

# サブエージェントの永続メモリにテンプレートを配置
mkdir -p .claude/agent-memory/careful-worker/
cp agent-memory-template.md .claude/agent-memory/careful-worker/MEMORY.md
```

## 前提条件

- Claude Code CLI（最新版）
- Git（チェックポイント・リバート用）
