# Ch07: Tool Design and ACI

Sample code for Chapter 7 of *Multi-Agent Development with Claude Code*.

## Files

### Working MCP Server Implementation

| File | Type | Description |
|------|------|-------------|
| `server.py` | FastMCP server | Internal knowledge base search server embodying the 6 ACI principles (~170 lines) |
| `pyproject.toml` | Project config | Dependency definitions for `mcp[cli]` and `pydantic` |

### Tool Schema Reference Examples

| File | Type | Description |
|------|------|-------------|
| `schemas/search-customers.json` | Tool schema | `response_format` verbosity control pattern |
| `schemas/search-logs.json` | Tool schema | Pagination (`limit`/`offset`) pattern |
| `schemas/list-issues.json` | Tool schema | `enum` filtering pattern |
| `schemas/search-knowledge-base.json` | Tool schema | Detailed `description` writing example |
| `schemas/read-tool.json` | Tool schema | Absolute path enforcement pattern (Claude Code example) |
| `schemas/grep-tool.json` | Tool schema | Output mode control pattern (Claude Code example) |

## Quick Start (Running server.py)

### 1. Install

```bash
cd ch07-tool-design-aci
uv sync
```

Or without `uv`:

```bash
pip install "mcp[cli]>=1.12" "pydantic>=2.0"
```

### 2. Register with Claude Code

```bash
claude mcp add kb --transport stdio -- uv run /absolute/path/to/server.py
```

Replace `/absolute/path/to/server.py` with the actual path on your machine.
After registration, run `/mcp` inside Claude Code to verify the `kb` server status.

### 3. Try It Out

In a Claude Code session, ask a question like:

```text
Show me the onboarding procedure
```

The `mcp__kb__search_articles` tool fires first in `concise` mode, returning just
article counts. Drill into a specific article with `mcp__kb__get_article_detail`
or by re-querying with `response_format=detailed`.

## ACI 6 Principles Mapped to server.py

| Principle | How server.py Implements It |
|-----------|---------------------------|
| 1. Choose the right tools | No `list_articles` dump — only `search_articles` with filtering |
| 2. Consolidate functionality | Category, keyword, and pagination combined in one tool |
| 3. Namespace with clear boundaries | Registered as `kb` → tools appear as `mcp__kb__search_articles` |
| 4. Return meaningful context | Human-readable IDs like `kb-deploy-002` instead of UUIDs |
| 5. Optimize token efficiency | `response_format` (concise/detailed) plus `limit`/`offset` |
| 6. Prompt-engineer tool descriptions | Docstring includes use cases, exclusions, and hints |

## Using the Tool Schema References

The JSON files in `schemas/` serve as reference patterns for designing your own
MCP server tool definitions. Each pattern maps to a corresponding section in
server.py:

- **Verbosity control**: `search-customers.json` ↔ `response_format` in server.py
- **Pagination**: `search-logs.json` ↔ `limit`/`offset` in server.py
- **Filtering**: `list-issues.json` ↔ `category` in server.py
- **Description writing**: `search-knowledge-base.json` ↔ docstring in server.py
- **Path safety**: `read-tool.json` — Claude Code built-in example
- **Output modes**: `grep-tool.json` — Claude Code built-in example

## Prerequisites

- Claude Code CLI (latest)
- Python 3.10+
- `mcp[cli]` 1.12+
