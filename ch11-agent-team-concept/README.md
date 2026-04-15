# Ch11: Getting Started with Agent Teams

Sample code for Chapter 11 of *Multi-Agent Development with Claude Code*.

## Files

| File | Type | Description |
|------|------|-------------|
| `settings-agent-teams.json` | JSON | `settings.json` config to enable the agent teams feature |
| `agents/security-reviewer.md` | Subagent definition | Security review subagent with restricted tool access |

## Usage

### Enabling Agent Teams

Merge the contents of `settings-agent-teams.json` into your project's `.claude/settings.json` or user settings at `~/.claude/settings.json`.

```bash
# Or set via environment variable
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

### Reusing Subagent Definitions as Teammates

Place `agents/security-reviewer.md` in `.claude/agents/`. The orchestrator can then reference it when spawning teammates.

```text
Using the security-reviewer agent type,
spawn a teammate to audit the authentication module.
```

## Prerequisites

- Claude Code CLI (v2.1.32 or later)
