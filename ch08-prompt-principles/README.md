# Ch08: Eight Principles of Agent Prompts

Sample code for Chapter 8 of *Multi-Agent Development with Claude Code*.

## Files

| File | Type | Description |
|------|------|-------------|
| `agents/debug-researcher.md` | Subagent | Debug agent that reports findings and reasoning in detail (Principle 1) |
| `agents/task-coordinator.md` | Subagent | Coordinator that allocates resources based on task complexity (Principle 3) |
| `agents/prompt-improver.md` | Subagent | Analyzes and improves subagent prompts (Principle 5) |
| `agents/methodical-researcher.md` | Subagent | Plans before investigating, then researches systematically (Principle 7) |
| `agents/code-reviewer.md` | Subagent | Code review agent applying all 8 principles |
| `CLAUDE-multiagent-policy.md` | CLAUDE.md template | Project-level multi-agent policy |
| `CLAUDE-delegation-rules.md` | CLAUDE.md template | Delegation rules template for subagents |

## Usage

Place subagent definition files in the `.claude/agents/` directory:

```bash
# Copy subagent definitions
cp agents/*.md .claude/agents/

# Append the CLAUDE.md template to your project's CLAUDE.md
cat CLAUDE-multiagent-policy.md >> CLAUDE.md
```

## Prerequisites

- Claude Code CLI (latest)
