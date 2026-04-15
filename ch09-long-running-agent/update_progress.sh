#!/usr/bin/env bash
# update_progress.sh -- Append a session entry to claude-progress.txt.
#
# Usage:
#   ./update_progress.sh "<completed work>" "<next steps>"
#
# Example:
#   ./update_progress.sh "Implemented JWT auth" "Add refresh tokens"
#
# Output format:
#   ## YYYY-MM-DD HH:MM <git-short-sha>
#   - Completed: <completed work>
#   - Commit: <sha> "<latest commit subject>"
#   - Next steps: <next steps>

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
    echo "- Completed: ${COMPLETED}"
    echo "- Commit: ${SHA} \"${SUBJECT}\""
    echo "- Next steps: ${NEXT_STEP}"
} >> "$PROGRESS_FILE"

echo "appended to ${PROGRESS_FILE}"
