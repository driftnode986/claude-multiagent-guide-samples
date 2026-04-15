## Graceful Degradation Rules (include in CLAUDE.md)

### When MCP servers are unavailable
- GitHub MCP unavailable -> use `gh` CLI commands instead
- Playwright MCP unavailable -> skip tests, flag for manual verification later
- Database MCP unavailable -> validate with local SQLite

### When all external services are unavailable
- Focus on work achievable with local tools only
- Record tasks with external dependencies as "blocked"
- Report the list of blocked tasks

### When context has degraded
- Record the current state in detail in the progress file
- Save current code with a Git commit
- Record "handoff notes for the next session" and terminate
