# Ch03 Demo Prompts

Prompts to reproduce the three hands-on examples from Chapter 3. Open `sample-codebase/` in Claude Code and try each one.

```bash
cd ch03-subagent-basics/sample-codebase
claude
```

The goal is to observe which built-in subagent Claude Code selects automatically. Verify via session logs (`/transcript`) or Hooks.

## Example 1: Codebase Investigation (Explore expected)

```text
Identify all authentication-related files in this project and summarize
how authentication is used in each file.
```

**What to observe**:

- Claude Code delegates investigation to the Explore subagent
- The main session context receives only the summary, not raw file contents
- Explore is read-only -- no files are modified

**Expected result**: Four files identified (`src/middleware/auth.ts`, `src/routes/protected.ts`, `src/utils/token.ts`, `tests/auth.test.ts`) with a brief role summary for each.

## Example 2: Parallel Review (multiple general-purpose subagents expected)

Using `sample-codebase/` as a simulated PR:

```text
Review src/middleware/auth.ts and src/utils/token.ts from three perspectives,
each handled by a separate subagent running in parallel:
1. Security vulnerabilities
2. Performance issues
3. Coding standard violations
Combine the results into a unified report.
```

**What to observe**:

- Claude Code spawns three general-purpose subagents with `run_in_background: true`
- Each subagent analyzes independently in its own context
- The main agent synthesizes the three results

**Expected result**: Separate findings for security (e.g., hardcoded `demo-cookie`), performance (e.g., O(1) lookup adequacy), and coding standards (e.g., naming, type definitions).

## Example 3: Git Worktree Isolation (isolation: worktree)

The worktree feature requires a Git repository. Clone the companion repo and launch Claude Code from within it:

```bash
git clone https://github.com/driftnode986/claude-multiagent-guide-samples.git
cd claude-multiagent-guide-samples/ch03-subagent-basics/sample-codebase
claude
```

If you want to try from a separate location, run `git init` there first (don't run `git init` inside the companion repo -- it would create a nested Git repository).

```text
Experiment with replacing auth.ts with a JWT-based implementation using
a Git worktree. Do not modify the main worktree.
```

**What to observe**:

- Claude Code spawns a subagent with `isolation: "worktree"`
- A temporary worktree is created; the main worktree remains unchanged
- On success, the worktree path and branch name are returned

**Expected result**: The original `auth.ts` is unchanged. A new branch contains the experimental JWT implementation.

## Notes

- These sample files intentionally omit TypeScript type resolution and won't compile. They're stubs designed for Explore to discover and summarize.
- Which subagent gets invoked depends on the Claude Code version and its selection logic. Rewording the prompt may trigger a different subagent.
- Examples 2 and 3 describe the *likely* behavior -- background spawning and worktree isolation aren't guaranteed. Check `/transcript` or Hooks to confirm actual behavior.
