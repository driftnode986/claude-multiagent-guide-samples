# 第9章: セッションをまたぐ長時間エージェント

「Claude Codeマルチエージェント実践ガイド」第9章のサンプルコードです。
Anthropic Engineering Blog（2025年11月）「Effective harnesses for long-running agents」で紹介されたハーネスをClaude Codeで動かすための最小実装を提供します。

## クイックスタート

```bash
# 1. スクリプトに実行権限を付与する
chmod +x init.sh update_progress.sh
chmod +x generate_features.py next_feature.py mark_passed.py

# 2. 長時間プロジェクト用のディレクトリを初期化する
./init.sh /path/to/your/project
cd /path/to/your/project

# 3. フィーチャーリストを編集する
$EDITOR features.txt

# 4. feature_list.json を再生成する（passes フラグは保持される）
python3 /path/to/generate_features.py features.txt feature_list.json

# 5. コーディングエージェントが各セッションで呼び出すコマンド
python3 next_feature.py            # 未完了の次のフィーチャーを取得する
# ...実装...
git add -A && git commit -m "feat: <説明>"
python3 mark_passed.py "<説明>"
./update_progress.sh "完了したこと" "次のステップ"
```

## ファイル一覧

### コアスクリプト（5ファイル）

| ファイル | 種別 | 説明 |
|---------|------|------|
| `init.sh` | bash | 初期化エージェント。features.txt → ファイル生成 → 初回コミット |
| `generate_features.py` | python | features.txt から feature_list.json を生成する。既存の passes は保持 |
| `next_feature.py` | python | feature_list.json から優先度最上位の未完了フィーチャーを返す |
| `mark_passed.py` | python | 指定フィーチャーの passes を true にする（完全一致、1件のみ） |
| `update_progress.sh` | bash | セッションエントリを claude-progress.txt に追記する |

### テンプレート / ヘルパー

| ファイル | 種別 | 説明 |
|---------|------|------|
| `feature_list.json` | JSON | フィーチャーリスト構造の例（init.sh の出力と同じスキーマ） |
| `claude-progress.txt` | テキスト | 進捗ファイルのエントリ例 |
| `CLAUDE-long-task.md` | テンプレート | 長時間タスク管理ルール（CLAUDE.md に追記して使用） |
| `agents/project-worker.md` | サブエージェント定義 | 永続メモリを持つ長時間プロジェクトワーカー |
| `long-run.sh` | bash | `claude --agent` を使ったループ実行スクリプト（コンテナ内推奨） |
| `NOTES-template.md` | テンプレート | 構造化メモ取りテンプレート |
| `checkpoint-rules.md` | テンプレート | Gitベースのチェックポイントルール |

## features.txt のフォーマット

```text
# functional: ユーザーがログインできる
- ログインフォームを開く
- メールアドレスとパスワードを入力する
- ログインボタンをクリックする
- ダッシュボードへのリダイレクトを確認する

# functional: ユーザーがログアウトできる
- ログアウトボタンをクリックする
- セッションが破棄されたことを確認する
```

- `# <カテゴリ>: <説明>` でフィーチャーを開始する
- `-` で始まる行はステップ
- 空行は区切り
- カテゴリは自由形式: functional、ui、api、perf など

## Anthropicの4要素との対応

| Anthropicの4要素 | 実装ファイル |
|----------------|------------|
| フィーチャーリスト | `feature_list.json` |
| 進捗ファイル | `claude-progress.txt` |
| 初期化スクリプト | `init.sh` |
| 初回コミット | init.sh 内の `git commit` |

## 動作要件

- Claude Code CLI（最新版）
- Python 3.10以上（`list[dict] | None` 型ヒント構文を使用）
- Git
- `git config user.name` / `git config user.email` の設定が必要

## 動作確認

書籍のリポジトリに含まれるスモークテストを実行できます。10ステップで全スクリプトを検証します。
