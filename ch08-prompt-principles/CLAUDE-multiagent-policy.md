# CLAUDE.md

## Multi-Agent Policy

### Delegation Criteria
- 1 file change: handle yourself
- 2-5 files: 1 subagent
- 6+ files: multiple subagents in parallel

### Required Information When Delegating
1. Concrete goal (1-2 sentences)
2. Output format (JSON / Markdown / bullet list)
3. Which tools to use
4. Work that is out of scope

### Search Strategy
- Start with a broad search, then narrow based on results
- Glob to understand file structure → Grep for specific code search

### Quality Standards
- Always verify subagent results
- Double-check "no issues found" reports from a different angle
- Never report uncertain information as fact
