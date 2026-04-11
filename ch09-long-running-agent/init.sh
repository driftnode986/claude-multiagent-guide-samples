#!/usr/bin/env bash
# init.sh — 長期実行プロジェクトの初期化エージェント。
#
# 最初のセッションで一度だけ実行する。次のものを生成する:
#   - feature_list.json (features.txt から生成)
#   - claude-progress.txt (進捗ログのヘッダー)
#   - AGENT_PROMPT.md (コーディングエージェント用プロンプト)
#   - current_tasks/ (タスクロックの置き場)
#   - agent_logs/ (long-run.sh のログ出力先)
#   - 初期 git コミット
#
# 既存ファイルは原則上書きしない。feature_list.json のみ
# generate_features.py が passes フラグを引き継いで再生成する。
#
# 使い方:
#   ./init.sh                # カレントを対象にする
#   ./init.sh /path/to/proj  # 指定ディレクトリを対象にする

set -euo pipefail

ROOT_DIR="${1:-.}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-python3}"

mkdir -p "$ROOT_DIR"
cd "$ROOT_DIR"

echo "=== 長期実行プロジェクトの初期化 ==="
echo "対象ディレクトリ: $(pwd)"

# [0/5] helper スクリプトを ROOT_DIR に配置 (worktree でも動くよう SCRIPT_DIR != ROOT_DIR を許容)
if [ "$SCRIPT_DIR" != "$(pwd)" ]; then
    for helper in generate_features.py next_feature.py mark_passed.py update_progress.sh; do
        if [ ! -f "$helper" ]; then
            cp "$SCRIPT_DIR/$helper" "$helper"
            chmod +x "$helper"
        fi
    done
    echo "[0/5] helper スクリプトを配置"
fi

# [1/5] git リポジトリの確認 (worktree の .git ファイルにも対応)
if ! git rev-parse --git-dir >/dev/null 2>&1; then
    echo "[1/5] git リポジトリを初期化"
    git init -q
else
    echo "[1/5] 既存の git リポジトリを使用"
fi

# [2/5] features.txt と feature_list.json
if [ ! -f features.txt ]; then
    echo "[2/5] features.txt が存在しないためテンプレートを作成"
    cat > features.txt <<'EOF'
# functional: ユーザーがログインできる
- ログインフォームを開く
- メールアドレスとパスワードを入力する
- ログインボタンをクリックする
- ダッシュボードにリダイレクトされることを確認する

# functional: ユーザーがログアウトできる
- ログアウトボタンをクリックする
- セッションが破棄されることを確認する
- ログイン画面にリダイレクトされることを確認する
EOF
fi
echo "[2/5] feature_list.json を generate_features.py で生成"
"$PYTHON" "$SCRIPT_DIR/generate_features.py" features.txt feature_list.json

# [3/5] claude-progress.txt
if [ ! -f claude-progress.txt ]; then
    echo "[3/5] claude-progress.txt を初期化"
    cat > claude-progress.txt <<'EOF'
# 長期実行プロジェクトの進捗ログ

このファイルは update_progress.sh が自動更新します。
各エントリは「日時 / 完了内容 / コミット / 次のステップ」を含みます。
EOF
else
    echo "[3/5] claude-progress.txt は既存のものを使用"
fi

# [4/5] AGENT_PROMPT.md と作業ディレクトリ
if [ ! -f AGENT_PROMPT.md ]; then
    echo "[4/5] AGENT_PROMPT.md を作成"
    cat > AGENT_PROMPT.md <<'EOF'
あなたは長期プロジェクトのコーディングエージェントです。

## セッションの進め方

1. `tail -20 claude-progress.txt` で前回までの作業を把握する
2. `git log --oneline -10` で最近のコミットを確認する
3. `python3 next_feature.py` で最優先の未完了 feature を取得する
4. その feature を1つだけ実装する。複数を一気にやらない
5. テストを実行し、緑になることを確認する
6. `git add -A && git commit -m "feat: <feature の description>"`
7. `python3 mark_passed.py "<feature の description>"` で完了を記録
8. `./update_progress.sh "<完了内容>" "<次のステップ>"` で進捗ログを追記

## 守るべきルール

- 1セッション 1 feature のみ。コンテキストが残っていても次に進まない
- テストが通らない状態でコミットしない
- feature_list.json の steps と description は変更しない
  (passes フラグのみ変更する)
- 不明点があれば NOTES.md に書き、次のセッションに引き継ぐ
EOF
else
    echo "[4/5] AGENT_PROMPT.md は既存のものを使用"
fi
mkdir -p current_tasks agent_logs

# [5/5] 初期コミット (現在の git config をそのまま使う)
if [ -z "$(git log --oneline 2>/dev/null || true)" ]; then
    echo "[5/5] 初期コミットを作成"
    git add features.txt feature_list.json claude-progress.txt AGENT_PROMPT.md
    if git commit -q -m "chore: initialize long-running agent harness"; then
        echo "      初期コミット完了"
    else
        echo "      WARNING: 初期コミットに失敗しました。" >&2
        echo "      git config user.name / user.email を設定してから" >&2
        echo "      手動で git commit してください。" >&2
    fi
else
    echo "[5/5] コミット履歴あり。初期コミットはスキップ"
fi

echo "=== 初期化完了 ==="
echo
echo "次のセッションから AGENT_PROMPT.md を使ってループ実行してください:"
echo "  ./long-run.sh"
