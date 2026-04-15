# Ch12: Agent Teams in Practice

Sample code for Chapter 12 of *Multi-Agent Development with Claude Code*.

## Files

| File | Type | Description |
|------|------|-------------|
| `claude-json-teammate-mode.json` | JSON | Teammate display mode setting for `~/.claude.json` |
| `settings-teammate-idle.json` | JSON | `settings.json` config for TeammateIdle hooks |
| `hooks/check-teammate-idle.sh` | Shell | Quality gate that runs tests when a teammate goes idle |
| `hooks/check-task-completed.sh` | Shell | Quality gate that checks lint and tests on task completion |

## Usage

### Display Mode Configuration

Merge the contents of `claude-json-teammate-mode.json` into `~/.claude.json`. Options are `"auto"` (default), `"in-process"`, or `"split-pane"`.

### Quality Gates via Hooks

1. Merge `settings-teammate-idle.json` into your project's `.claude/settings.json`
2. Copy the scripts under `hooks/` to `.claude/hooks/`
3. Grant execute permissions: `chmod +x .claude/hooks/*.sh`

Hooks return exit code `2` to send feedback and instruct the teammate to continue working.

## Prerequisites

- Claude Code CLI (latest version)
- A Node.js project with working `npm test` / `npm run lint`
