# 第13章: エージェントのパフォーマンス評価

「Claude Codeマルチエージェント実践ガイド」第13章のサンプルコードです。

## ファイル

| ファイル | 種別 | 説明 |
|---------|------|------|
| `eval-tasks/fix-auth-bypass.yml` | YAML | 認証バイパス修正の評価タスク定義（合否基準付き） |
| `eval-tasks/auth.py` | Python | テスト対象コード（空パスワードによるバイパスバグを含む） |
| `eval-tasks/test_empty_pw_rejected.py` | Python | 空パスワードが拒否されることを検証するグレーダー |
| `eval-tasks/test_null_pw_rejected.py` | Python | nullパスワードが拒否されることを検証するグレーダー |
| `agents/eval-runner.md` | サブエージェント定義 | 評価タスクを実行して結果を記録するエージェント |
| `settings-regression-hooks.json` | JSON | リグレッション検出フック用の `settings.json` 設定 |

## 使い方

### 評価タスクの定義

`eval-tasks/fix-auth-bypass.yml` をテンプレートとして、プロジェクト固有の評価タスクを作成します。各タスクには以下が含まれます。

- `id`: 一意の識別子
- `desc`: 曖昧さのないタスクの説明
- `graders`: 決定論的なテストまたは状態チェックを使った合否基準

### 評価の実行

`agents/eval-runner.md` を `.claude/agents/` に配置してサブエージェントとして呼び出します。

### リグレッション検出

`settings-regression-hooks.json` を `.claude/settings.json` にマージすると、ファイルの書き込みや編集の前に毎回リグレッションスイートが実行されます。プロジェクトに合わせた `scripts/run-regression-suite.sh` を作成してください。

## 動作要件

- Claude Code CLI（最新版）
- プロジェクト固有のテストスイート
