# Ch08: エージェントプロンプトの8原則

書籍「Claude Code マルチエージェント実践ガイド」第8章のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `agents/debug-researcher.md` | サブエージェント | 調査結果と推論過程を詳細に報告するデバッグ用エージェント（原則1） |
| `agents/task-coordinator.md` | サブエージェント | タスクの複雑さに応じてリソースを配分するコーディネーター（原則3） |
| `agents/prompt-improver.md` | サブエージェント | サブエージェントのプロンプトを分析・改善する（原則5） |
| `agents/methodical-researcher.md` | サブエージェント | 計画を立ててから体系的に調査する（原則7） |
| `agents/code-reviewer.md` | サブエージェント | 8原則を適用したコードレビューエージェント |
| `CLAUDE-multiagent-policy.md` | CLAUDE.mdテンプレート | プロジェクトレベルのマルチエージェント方針 |
| `CLAUDE-delegation-rules.md` | CLAUDE.mdテンプレート | サブエージェントへの委譲ルールテンプレート |

## 使い方

サブエージェント定義ファイルは `.claude/agents/` ディレクトリに配置して使用します。

```bash
# サブエージェント定義を配置
cp agents/*.md .claude/agents/

# CLAUDE.mdテンプレートの内容をプロジェクトのCLAUDE.mdに追記
cat CLAUDE-multiagent-policy.md >> CLAUDE.md
```

## 前提条件

- Claude Code CLI（最新版）
