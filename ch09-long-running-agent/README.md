# Ch09: Long-Running Agents Across Sessions

Sample code for Chapter 9 of *Multi-Agent Development with Claude Code*.
Provides a minimal implementation to run the harness described in
Anthropic's Engineering Blog (Nov 2025) "Effective harnesses for long-running agents"
with Claude Code.

## Quick Start

```bash
# 1. Make scripts executable
chmod +x init.sh update_progress.sh
chmod +x generate_features.py next_feature.py mark_passed.py

# 2. Initialize a long-running project directory
./init.sh /path/to/your/project
cd /path/to/your/project

# 3. Edit the feature list
$EDITOR features.txt

# 4. Regenerate feature_list.json (passes flags are preserved)
python3 /path/to/generate_features.py features.txt feature_list.json

# 5. Commands the coding agent calls each session
python3 next_feature.py            # Get the next incomplete feature
# ...implement...
git add -A && git commit -m "feat: <description>"
python3 mark_passed.py "<description>"
./update_progress.sh "What was completed" "Next steps"
```

## File Listing

### Core Scripts (5 files)

| File | Type | Description |
|------|------|-------------|
| `init.sh` | bash | Initialization agent. features.txt -> files -> initial commit |
| `generate_features.py` | python | Generate feature_list.json from features.txt. Preserves existing passes |
| `next_feature.py` | python | Return the highest-priority incomplete feature from feature_list.json |
| `mark_passed.py` | python | Set passes to true for the specified feature (exact match, single result only) |
| `update_progress.sh` | bash | Append a session entry to claude-progress.txt |

### Templates / Helpers

| File | Type | Description |
|------|------|-------------|
| `feature_list.json` | JSON | Feature list structure example (same schema as init.sh output) |
| `claude-progress.txt` | text | Progress file entry example |
| `CLAUDE-long-task.md` | template | Long-running task management rules (append to CLAUDE.md) |
| `agents/project-worker.md` | subagent definition | Long-running project worker with persistent memory |
| `long-run.sh` | bash | Loop execution script using `claude --agent` (recommended inside containers) |
| `NOTES-template.md` | template | Structured note-taking template |
| `checkpoint-rules.md` | template | Git-based checkpoint rules |

## features.txt Format

```text
# functional: User can log in
- Open the login form
- Enter email and password
- Click the login button
- Verify redirect to dashboard

# functional: User can log out
- Click the logout button
- Verify the session is destroyed
```

- `# <category>: <description>` starts a feature
- Lines starting with `-` are steps
- Blank lines are separators
- Categories are free-form: functional, ui, api, perf, etc.

## Mapping to the Four Elements

| Anthropic's Four Elements | Implementation File |
|---|---|
| Feature list | `feature_list.json` |
| Progress file | `claude-progress.txt` |
| Initialization script | `init.sh` |
| Initial commit | `git commit` inside init.sh |

## Prerequisites

- Claude Code CLI (latest version)
- Python 3.10+ (uses `list[dict] | None` type hint syntax)
- Git
- `git config user.name` / `git config user.email` must be set

## Verification

You can run the smoke test from the book repository. It validates all scripts in 10 steps.
