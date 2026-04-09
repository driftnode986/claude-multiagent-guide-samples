# Ch11: エージェントチームの概念と有効化

書籍「Claude Code マルチエージェント実践ガイド」第11章のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `settings-agent-teams.json` | JSON | エージェントチーム機能を有効化する `settings.json` 設定 |
| `agents/security-reviewer.md` | サブエージェント定義 | セキュリティレビュー用サブエージェント（ツール制限付き） |

## 使い方

### エージェントチームの有効化

`settings-agent-teams.json` の内容を、プロジェクトの `.claude/settings.json` またはユーザー設定 `~/.claude/settings.json` にマージしてください。

```bash
# または環境変数で設定
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

### サブエージェント定義のチームメイトへの再利用

`agents/security-reviewer.md` を `.claude/agents/` に配置すると、チームメイト生成時に参照できます。

```text
security-reviewer エージェントタイプを使って、
認証モジュールを監査するチームメイトを生成してください。
```

## 前提条件

- Claude Code CLI（v2.1.32以降）
