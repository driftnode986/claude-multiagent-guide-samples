# Ch09: セッションをまたぐ長期エージェント

書籍「Claude Code マルチエージェント実践ガイド」第9章のサンプルコードです。
Anthropic Engineering Blog (2025-11)「Effective harnesses for long-running agents」の
ハーネスを Claude Code で動かすための最小実装を提供します。

## クイックスタート

```bash
# 1. このディレクトリのスクリプトをパスに置く
chmod +x init.sh update_progress.sh
chmod +x generate_features.py next_feature.py mark_passed.py

# 2. 長期プロジェクトのディレクトリを初期化
./init.sh /path/to/your/project
cd /path/to/your/project

# 3. 機能リストを編集
$EDITOR features.txt

# 4. feature_list.json を再生成（passes は引き継がれる）
python3 /path/to/generate_features.py features.txt feature_list.json

# 5. 各セッションでコーディングエージェントが呼ぶコマンド
python3 next_feature.py            # 次の未完了 feature を取得
# ...実装...
git add -A && git commit -m "feat: <description>"
python3 mark_passed.py "<description>"
./update_progress.sh "完了内容" "次のステップ"
```

## ファイル一覧

### コアスクリプト (5本)

| ファイル | 種類 | 説明 |
|---------|------|------|
| `init.sh` | bash | 初期化エージェント。features.txt → 各種ファイル → 初期コミット |
| `generate_features.py` | python | features.txt から feature_list.json を生成。passes 引き継ぎ付き |
| `next_feature.py` | python | feature_list.json から最優先の未完了 feature を返す |
| `mark_passed.py` | python | 指定 feature の passes を true に切替（完全一致+1件限定） |
| `update_progress.sh` | bash | claude-progress.txt にセッションエントリを追記 |

### テンプレート / 補助

| ファイル | 種類 | 説明 |
|---------|------|------|
| `feature_list.json` | JSON | 機能リスト構造例（init.sh が生成するスキーマと同形式） |
| `claude-progress.txt` | テキスト | 進捗ファイルのエントリ例 |
| `CLAUDE-long-task.md` | テンプレート | 長期タスク管理ルール（CLAUDE.md に追記する内容） |
| `agents/project-worker.md` | サブエージェント定義 | 永続メモリを活用する長期プロジェクト作業者 |
| `long-run.sh` | bash | `claude --agent` によるループ実行スクリプト（コンテナ内推奨） |
| `NOTES-template.md` | テンプレート | 構造化ノートテイキングのテンプレート |
| `checkpoint-rules.md` | テンプレート | Gitベースのチェックポイントルール |

## features.txt の書式

```text
# functional: ユーザーがログインできる
- メールアドレスとパスワードを入力する
- ログインボタンをクリックする
- ダッシュボードにリダイレクトされることを確認する

# functional: ユーザーがログアウトできる
- ログアウトボタンをクリックする
- セッションが破棄されることを確認する
```

- `# <category>: <description>` で feature が始まる
- `-` で始まる行が steps
- 空行は区切り
- category は functional / ui / api / perf など自由

## 4要素との対応

| Anthropic の4要素 | 本実装のファイル |
|---|---|
| 機能リスト | `feature_list.json` |
| 進捗ファイル | `claude-progress.txt` |
| 初期化スクリプト | `init.sh` |
| 初期コミット | init.sh 内の `git commit` |

## 前提条件

- Claude Code CLI（最新版）
- Python 3.10 以上（type hints の `list[dict] | None` 構文を使用）
- Git
- 事前に `git config user.name` / `git config user.email` を設定

## 動作確認

書籍リポジトリから smoke test を流せます。10ステップで全スクリプトの整合を検証します。
