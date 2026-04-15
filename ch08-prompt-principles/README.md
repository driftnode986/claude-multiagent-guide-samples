# 第8章: エージェントプロンプトの8原則

「Claude Codeマルチエージェント実践ガイド」第8章のサンプルコードです。

## ファイル

| ファイル | 種別 | 説明 |
|---------|------|------|
| `agents/debug-researcher.md` | サブエージェント | 発見内容と推論を詳細にレポートするデバッグエージェント（原則1） |
| `agents/task-coordinator.md` | サブエージェント | タスクの複雑さに基づいてリソースを割り当てるコーディネーター（原則3） |
| `agents/prompt-improver.md` | サブエージェント | サブエージェントのプロンプトを分析・改善するエージェント（原則5） |
| `agents/methodical-researcher.md` | サブエージェント | 計画を立ててから体系的に調査するエージェント（原則7） |
| `agents/code-reviewer.md` | サブエージェント | 8原則を全て適用したコードレビューエージェント |
| `CLAUDE-multiagent-policy.md` | CLAUDE.md テンプレート | プロジェクトレベルのマルチエージェントポリシー |
| `CLAUDE-delegation-rules.md` | CLAUDE.md テンプレート | サブエージェント向けの委譲ルールテンプレート |

## 使い方

サブエージェント定義ファイルを `.claude/agents/` ディレクトリに配置します。

```bash
# サブエージェント定義をコピーする
cp agents/*.md .claude/agents/

# CLAUDE.md テンプレートをプロジェクトの CLAUDE.md に追記する
cat CLAUDE-multiagent-policy.md >> CLAUDE.md
```

## 動作要件

- Claude Code CLI（最新版）
