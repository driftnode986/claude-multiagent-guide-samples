# 第11章: エージェントチームの始め方

「Claude Codeマルチエージェント実践ガイド」第11章のサンプルコードです。

## ファイル

| ファイル | 種別 | 説明 |
|---------|------|------|
| `settings-agent-teams.json` | JSON | エージェントチーム機能を有効にする `settings.json` の設定 |
| `agents/security-reviewer.md` | サブエージェント定義 | ツールアクセスを制限したセキュリティレビューサブエージェント |

## 使い方

### エージェントチームの有効化

`settings-agent-teams.json` の内容をプロジェクトの `.claude/settings.json` またはユーザー設定の `~/.claude/settings.json` にマージします。

```bash
# または環境変数で設定する
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

### サブエージェント定義をチームメンバーとして再利用する

`agents/security-reviewer.md` を `.claude/agents/` に配置します。オーケストレーターはチームメンバーをスポーンする際にこれを参照できます。

```text
security-reviewer エージェントタイプを使って、
認証モジュールを監査するチームメンバーをスポーンしてください。
```

## 動作要件

- Claude Code CLI（v2.1.32 以降）
