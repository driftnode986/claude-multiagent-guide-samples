# Ch06: オーケストレーター設計

書籍「Claude Code マルチエージェント実践ガイド」第6章のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `agents/coordinator.md` | サブエージェント定義 | カスタムオーケストレーター（`claude --agent`で起動） |
| `CLAUDE-delegation-policy.md` | CLAUDE.md記述例 | プロジェクトのCLAUDE.mdに追加する委譲ルールの例 |

## 使い方

### カスタムオーケストレーターの起動

```bash
# coordinator.md を .claude/agents/ に配置後
claude --agent coordinator
```

`coordinator`はOpusモデルで動作し、タスクの複雑さに応じてサブエージェントへの委譲を判断します。

### CLAUDE.mdへの委譲ルール追加

`CLAUDE-delegation-policy.md`の内容をプロジェクトの`CLAUDE.md`に追記すると、メインセッションの振る舞いを誘導できます。

```bash
cat CLAUDE-delegation-policy.md >> your-project/CLAUDE.md
```

## 前提条件

- Claude Code CLI（最新版）
- 委譲先のサブエージェントが`.claude/agents/`に配置済みであること。本 repo では ch04 に `code-reviewer.md` / `test-writer.md` / `project-expert.md` / `security-auditor.md` の4つを用意しているので、必要なものを `.claude/agents/` にコピーするか、`CLAUDE-delegation-policy.md` 側の委譲ルールを既存のエージェントに合わせて調整してください
