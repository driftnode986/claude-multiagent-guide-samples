# Ch05: Connecting Subagents to External Tools via MCP

Sample code for Chapter 5 of "Multi-Agent Development with Claude Code."

## Files

| File | Type | Description |
|------|------|-------------|
| `agents/web-scraper.md` | Subagent definition | Web scraping agent using Playwright MCP |
| `agents/pr-reviewer.md` | Subagent definition | PR code review agent using GitHub MCP |
| `agents/deployment-checker.md` | Subagent definition | Post-deploy verification agent using Playwright + Datadog MCP |
| `scripts/validate-readonly-query.sh` | Shell script | PreToolUse hook that blocks SQL write operations |

## Usage

### Place the subagent definitions

Copy the `.md` files into your project's `.claude/agents/` directory:

```bash
cp agents/*.md your-project/.claude/agents/
```

### Place the validation script

```bash
cp scripts/validate-readonly-query.sh your-project/scripts/
chmod +x your-project/scripts/validate-readonly-query.sh
```

### Invoke a subagent

Describe the task in natural language from the main session -- Claude Code selects the appropriate subagent automatically:

```
You: Scrape all product names and prices from https://example.com/products
You: Review PR #42
```

## Prerequisites

- Claude Code CLI (latest version)
- Node.js (to start MCP servers via npx)
- GitHub MCP: GitHub authentication configured
- Validation script: jq installed
