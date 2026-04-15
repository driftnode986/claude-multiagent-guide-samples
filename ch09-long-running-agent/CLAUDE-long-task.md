# CLAUDE.md

## Long-Running Task Management

### Progress File
- Record work logs in `claude-progress.txt`
- Each entry must include: timestamp, completed work, next steps

### Work Rules
1. At session start, read `claude-progress.txt` and `git log`
2. Pick the highest-priority incomplete task
3. After completing a task, run tests to verify
4. Commit to Git and update the progress file
5. Keep the environment clean (build must pass)
