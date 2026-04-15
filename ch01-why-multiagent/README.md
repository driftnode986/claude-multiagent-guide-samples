# Ch01: The Case for Multi-Agent Systems

Companion code for Chapter 1 of *Multi-Agent Development with Claude Code*.

## Files

| File | Type | Description |
|------|------|-------------|
| `agent-harness.sh` | Shell | Agent harness from the C compiler project (infinite loop execution) |
| `AGENT_PROMPT.md` | Markdown | Agent instruction prompt (loaded by `agent-harness.sh`) |

## Usage

`agent-harness.sh` demonstrates the harness structure used in Anthropic's C compiler project. Each agent runs in an infinite loop inside a Docker container, autonomously selecting and executing tasks.

```bash
# Ensure AGENT_PROMPT.md is in the same directory
bash agent-harness.sh
```

> **Warning**: This script uses `--dangerously-skip-permissions`. Exercise caution when running in production environments.

## Prerequisites

- Claude Code CLI (latest version)
- Git
- Docker (for production use)
