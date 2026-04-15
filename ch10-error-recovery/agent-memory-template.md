# .claude/agent-memory/careful-worker/MEMORY.md

## Past Failure Patterns

### Authentication Module Changes
- Changes to auth/ have a wide blast radius
- Always investigate dependencies before modifying
- Incremental changes recommended (one file at a time)

### Database Schema Changes
- Take a backup before running migrations
- Run in the test environment first
