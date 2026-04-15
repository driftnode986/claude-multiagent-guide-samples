# Appendix A: Quick Reference Templates

Companion files for Appendix A of *Multi-Agent Development with Claude Code*.

## Files

| File | Type | Description |
|------|------|-------------|
| `agent-definition-template.md` | Subagent definition | YAML frontmatter + Markdown body template |
| `agent-tool-params.json` | JSON | Parameter reference for the `Agent` tool |
| `mcp-inline-template.yml` | YAML | Inline MCP server definition template |

## Usage

### Creating a Subagent Definition

Copy `agent-definition-template.md` into `.claude/agents/` in your project. Replace the `name`, `description`, `model`, and `tools` fields with your own values. The Markdown body becomes the subagent's system prompt.

### Agent Tool Parameters

`agent-tool-params.json` shows the parameter structure used when Claude Code spawns a subagent internally. The `prompt` field is the most important -- it contains the detailed instructions for the subagent.

### MCP Inline Definition

`mcp-inline-template.yml` is a template for defining MCP servers inline within a subagent definition. Use `${API_KEY}` syntax for environment variable references.

## Prerequisites

- Claude Code CLI (latest version)
