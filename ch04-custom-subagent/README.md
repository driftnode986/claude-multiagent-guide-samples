# Ch04: Building Custom Subagents

Sample code for Chapter 4 of *Multi-Agent Development with Claude Code*.

## Files

| File | Type | Description |
|------|------|-------------|
| `agents/code-reviewer.md` | Subagent definition | Basic code review agent |
| `agents/test-writer.md` | Subagent definition | Automated test generation agent |
| `agents/security-auditor.md` | Subagent definition | OWASP Top 10 security audit agent |
| `agents/project-expert.md` | Subagent definition | Project knowledge agent with persistent memory |
| `scripts/validate-readonly-query.sh` | Shell | PreToolUse hook: blocks SQL write operations |

## Usage

### Installing Subagent Definitions

Copy the files from `agents/` into your project's `.claude/agents/` directory:

```bash
mkdir -p .claude/agents
cp agents/*.md .claude/agents/
```

Claude Code automatically discovers and selects subagents based on task context.

### Installing the Validation Script

`scripts/validate-readonly-query.sh` is used as a PreToolUse hook for the `db-reader` subagent:

```bash
mkdir -p scripts
cp scripts/validate-readonly-query.sh scripts/
chmod +x scripts/validate-readonly-query.sh
```

## Prerequisites

- Claude Code CLI (latest version)
- jq (used by the validation script)
