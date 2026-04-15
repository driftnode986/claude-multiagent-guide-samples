# 第6章: オーケストレーターの設計

「Claude Codeマルチエージェント実践ガイド」第6章のサンプルコードです。

## ファイル

| ファイル | 種別 | 説明 |
|---------|------|------|
| `agents/coordinator.md` | サブエージェント定義 | カスタムオーケストレーター（`claude --agent` で起動） |
| `CLAUDE-delegation-policy.md` | CLAUDE.md の例 | プロジェクトの `CLAUDE.md` に追加する委譲ルール |

## 使い方

### カスタムオーケストレーターの起動

```bash
# coordinator.md を .claude/agents/ に配置してから実行
claude --agent coordinator
```

`coordinator` は Opus モデルで動作し、タスクの複雑さに基づいてサブエージェントへの委譲タイミングを判断します。

### CLAUDE.md への委譲ルールの追加

`CLAUDE-delegation-policy.md` の内容をプロジェクトの `CLAUDE.md` に追記することで、メインセッションの委譲動作を制御できます。

```bash
cat CLAUDE-delegation-policy.md >> your-project/CLAUDE.md
```

## 動作要件

- Claude Code CLI（最新版）
- コーディネーターを起動する前に、サブエージェントを `.claude/agents/` に配置しておく必要があります。このリポジトリでは `code-reviewer.md` / `test-writer.md` / `project-expert.md` / `security-auditor.md` を第4章で提供しています。必要なものを `.claude/agents/` にコピーするか、`CLAUDE-delegation-policy.md` の委譲ルールを既存のエージェントに合わせて修正してください。
