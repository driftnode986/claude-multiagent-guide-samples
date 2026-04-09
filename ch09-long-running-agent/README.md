# Ch09: セッションをまたぐ長期エージェント

書籍「Claude Code マルチエージェント実践ガイド」第9章のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `feature_list.json` | JSON | 機能リストの構造例（初期化エージェントが生成） |
| `claude-progress.txt` | テキスト | 進捗ファイルのエントリ例 |
| `init.sh` | シェルスクリプト | 環境セットアップスクリプト（初期化エージェントが生成） |
| `CLAUDE-long-task.md` | CLAUDE.mdテンプレート | 長期タスク管理のルール |
| `agents/project-worker.md` | サブエージェント | 永続メモリを活用する長期プロジェクト作業者 |
| `long-run.sh` | シェルスクリプト | `claude --agent`によるループ実行スクリプト |
| `NOTES-template.md` | テンプレート | 構造化ノートテイキングのテンプレート |
| `checkpoint-rules.md` | CLAUDE.mdテンプレート | Gitベースのチェックポイントルール |

## 使い方

```bash
# サブエージェント定義を配置
cp agents/*.md .claude/agents/

# ループ実行スクリプトを使用（コンテナ内推奨）
chmod +x long-run.sh
./long-run.sh

# CLAUDE.mdテンプレートの内容をプロジェクトに追記
cat CLAUDE-long-task.md >> CLAUDE.md
```

## 前提条件

- Claude Code CLI（最新版）
- Git（チェックポイント用）
