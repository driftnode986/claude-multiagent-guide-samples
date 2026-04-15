# Ch10: Error Recovery and Failure Mode Classification

Sample code for Chapter 10 of *Multi-Agent Development with Claude Code*.

## File Listing

| File | Type | Description |
|------|------|-------------|
| `recovery-strategies.yml` | YAML | Four failure mode categories with recovery strategies |
| `agents/risky-refactor.md` | subagent | Execute risky refactoring in an isolated worktree |
| `agents/resilient-worker.md` | subagent | Error-resilient worker agent (with hooks) |
| `agents/careful-worker.md` | subagent | Human-in-the-loop agent that stops when uncertain |
| `graceful-degradation.yml` | YAML | Four levels of graceful degradation |
| `CLAUDE-degrade-rules.md` | CLAUDE.md template | Graceful degradation rules |
| `failure-log-template.md` | template | Failure log template |
| `agent-memory-template.md` | template | Subagent persistent memory MEMORY.md template |

## Usage

```bash
# Place subagent definitions
cp agents/*.md .claude/agents/

# Append graceful degradation rules to CLAUDE.md
cat CLAUDE-degrade-rules.md >> CLAUDE.md

# Use the failure log template
cp failure-log-template.md docs/failure-log.md

# Place persistent memory template for a subagent
mkdir -p .claude/agent-memory/careful-worker/
cp agent-memory-template.md .claude/agent-memory/careful-worker/MEMORY.md
```

## Prerequisites

- Claude Code CLI (latest version)
- Git (for checkpointing and reverts)
