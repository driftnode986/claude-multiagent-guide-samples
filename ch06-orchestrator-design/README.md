# Ch06: Orchestrator Design

Sample code for Chapter 6 of "Multi-Agent Development with Claude Code."

## Files

| File | Type | Description |
|------|------|-------------|
| `agents/coordinator.md` | Subagent definition | Custom orchestrator (launched with `claude --agent`) |
| `CLAUDE-delegation-policy.md` | CLAUDE.md example | Delegation rules to add to your project's `CLAUDE.md` |

## Usage

### Launch the custom orchestrator

```bash
# Place coordinator.md in .claude/agents/, then:
claude --agent coordinator
```

The `coordinator` runs on the Opus model and decides when to delegate to subagents based on task complexity.

### Add delegation rules to CLAUDE.md

Append the contents of `CLAUDE-delegation-policy.md` to your project's `CLAUDE.md` to guide the main session's delegation behavior:

```bash
cat CLAUDE-delegation-policy.md >> your-project/CLAUDE.md
```

## Prerequisites

- Claude Code CLI (latest version)
- Subagents must be placed in `.claude/agents/` before launching the coordinator. This repo provides `code-reviewer.md` / `test-writer.md` / `project-expert.md` / `security-auditor.md` in ch04. Copy the ones you need to `.claude/agents/`, or adjust the delegation rules in `CLAUDE-delegation-policy.md` to match your existing agents.
