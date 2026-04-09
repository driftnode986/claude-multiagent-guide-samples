# Ch13: 評価・品質保証

書籍「Claude Code マルチエージェント実践ガイド」第13章のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `eval-tasks/fix-auth-bypass.yml` | YAML | 認証バイパス修正タスクの評価定義（pass/fail基準付き） |
| `agents/eval-runner.md` | サブエージェント定義 | 評価タスクを実行し結果を記録するエージェント |
| `settings-regression-hooks.json` | JSON | リグレッション検出 Hooks の `settings.json` 設定 |

## 使い方

### 評価タスクの定義

`eval-tasks/fix-auth-bypass.yml` を参考に、プロジェクト固有の評価タスクを作成してください。各タスクには以下を含めます:

- `id`: 一意の識別子
- `desc`: 曖昧さのないタスク説明
- `graders`: 決定的テストや状態チェックによる合否判定

### 評価の実行

`agents/eval-runner.md` を `.claude/agents/` に配置し、サブエージェントとして呼び出します。

### リグレッション検出

`settings-regression-hooks.json` の内容を `.claude/settings.json` にマージすると、ファイル書き込み・編集の前にリグレッションスイートが実行されます。`scripts/run-regression-suite.sh` は別途プロジェクトに合わせて作成してください。

## 前提条件

- Claude Code CLI（最新版）
- プロジェクト固有のテストスイート
