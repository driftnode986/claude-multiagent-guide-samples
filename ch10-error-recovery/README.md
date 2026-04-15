# 第10章: エラーリカバリーと障害モードの分類

「Claude Codeマルチエージェント実践ガイド」第10章のサンプルコードです。

## ファイル一覧

| ファイル | 種別 | 説明 |
|---------|------|------|
| `recovery-strategies.yml` | YAML | 4つの障害モードカテゴリとリカバリー戦略 |
| `agents/risky-refactor.md` | サブエージェント | 分離されたワークツリーでリスクの高いリファクタリングを実行する |
| `agents/resilient-worker.md` | サブエージェント | エラー耐性を持つワーカーエージェント（フック付き） |
| `agents/careful-worker.md` | サブエージェント | 不確かな場合に停止するヒューマンインザループエージェント |
| `graceful-degradation.yml` | YAML | 4段階のグレースフルデグラデーション |
| `CLAUDE-degrade-rules.md` | CLAUDE.md テンプレート | グレースフルデグラデーションルール |
| `failure-log-template.md` | テンプレート | 障害ログテンプレート |
| `agent-memory-template.md` | テンプレート | サブエージェントの永続メモリ MEMORY.md テンプレート |

## 使い方

```bash
# サブエージェント定義を配置する
cp agents/*.md .claude/agents/

# グレースフルデグラデーションルールを CLAUDE.md に追記する
cat CLAUDE-degrade-rules.md >> CLAUDE.md

# 障害ログテンプレートを使用する
cp failure-log-template.md docs/failure-log.md

# サブエージェント用の永続メモリテンプレートを配置する
mkdir -p .claude/agent-memory/careful-worker/
cp agent-memory-template.md .claude/agent-memory/careful-worker/MEMORY.md
```

## 動作要件

- Claude Code CLI（最新版）
- Git（チェックポイントと巻き戻しに使用）
