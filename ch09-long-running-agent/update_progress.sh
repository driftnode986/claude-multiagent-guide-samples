#!/usr/bin/env bash
# update_progress.sh — claude-progress.txt にセッションエントリを追記する。
#
# 使い方:
#   ./update_progress.sh "<完了内容>" "<次のステップ>"
#
# 例:
#   ./update_progress.sh "JWT認証を実装" "リフレッシュトークンの追加"
#
# 出力フォーマット:
#   ## YYYY-MM-DD HH:MM <git-short-sha>
#   - 完了: <完了内容>
#   - コミット: <sha> "<最新コミットの subject>"
#   - 次のステップ: <次のステップ>

set -euo pipefail

if [ "$#" -ne 2 ]; then
    echo "usage: $0 <completed> <next-step>" >&2
    exit 2
fi

COMPLETED="$1"
NEXT_STEP="$2"
PROGRESS_FILE="${PROGRESS_FILE:-claude-progress.txt}"

if ! command -v git >/dev/null 2>&1; then
    echo "error: git is not installed" >&2
    exit 1
fi

SHA=$(git rev-parse --short=7 HEAD 2>/dev/null || echo "uncommitted")
SUBJECT=$(git log -1 --pretty=%s 2>/dev/null || echo "(no commits yet)")
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')

{
    echo
    echo "## ${TIMESTAMP} ${SHA}"
    echo "- 完了: ${COMPLETED}"
    echo "- コミット: ${SHA} \"${SUBJECT}\""
    echo "- 次のステップ: ${NEXT_STEP}"
} >> "$PROGRESS_FILE"

echo "appended to ${PROGRESS_FILE}"
