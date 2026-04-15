# Multi-Agent Development with Claude Code -- Companion Code

Sample code repository for the book *Multi-Agent Development with Claude Code*.

## Structure

| Directory | Chapter | Contents | Files |
|-----------|---------|----------|-------|
| `ch01-why-multiagent/` | Ch1 | The Case for Multi-Agent Systems | 2 |
| `ch02-five-patterns/` | Ch2 | Five Workflow Patterns | 4 |
| `ch03-subagent-basics/` | Ch3 | How Subagents Work | 5 |
| `ch04-custom-subagent/` | Ch4 | Building Custom Subagents | 5 |
| `ch05-subagent-mcp/` | Ch5 | Connecting Subagents to External Tools via MCP | 4 |
| `ch06-orchestrator-design/` | Ch6 | Orchestrator Design | 2 |
| `ch07-tool-design-aci/` | Ch7 | Designing Tools for Agents | 6 |
| `ch08-prompt-principles/` | Ch8 | Writing Effective Agent Prompts | 7 |
| `ch09-long-running-agent/` | Ch9 | Managing Long-Running Agent Sessions | 7 |
| `ch10-error-recovery/` | Ch10 | Error Recovery and Failure Modes | 8 |
| `ch11-agent-team-concept/` | Ch11 | Getting Started with Agent Teams | 2 |
| `ch12-parallel-development/` | Ch12 | Agent Teams in Practice | 4 |
| `ch13-evaluation-qa/` | Ch13 | Evaluating Agent Performance | 3 |
| `ch14-production-reliability/` | Ch14 | Production Reliability | 3 |
| `appendix-a-reference/` | App A | Quick Reference Templates | 3 |

## File Types

| Extension | Location | Description |
|-----------|----------|-------------|
| `agents/*.md` | Per chapter | Custom subagent definitions (place in `.claude/agents/` to use) |
| `*.sh` | Per chapter | Shell scripts (harnesses, hooks, validation) |
| `schemas/*.json` | Ch7 | Tool definition JSON schemas |
| `*.json` | Per chapter | Claude Code configuration files (`settings.json`, etc.) |
| `*.yml` | Per chapter | Strategy and task definitions |
| `CLAUDE-*.md` | Per chapter | `CLAUDE.md` templates (place in project root to use) |

## Quick Start

```bash
git clone https://github.com/driftnode986/claude-multiagent-guide-samples.git
cd claude-multiagent-guide-samples
```

### Using a Subagent

```bash
# Example: copy the test writer from Ch4 into your project
cp ch04-custom-subagent/agents/test-writer.md your-project/.claude/agents/
```

### Enabling Agent Teams

```bash
# Review the Ch11 settings and update your own settings.json
cat ch11-agent-team-concept/settings-agent-teams.json
```

## Requirements

- Claude Code CLI (latest version)
- macOS / Linux

## Usage

See the `README.md` in each directory for chapter-specific instructions.

## Book Information

- **Title**: Multi-Agent Development with Claude Code
- **Author**: Makoto Makino
