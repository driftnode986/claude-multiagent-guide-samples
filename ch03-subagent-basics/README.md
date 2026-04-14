# Ch03: How Subagents Work

Sample code for Chapter 3 of *Multi-Agent Development with Claude Code*.

## Overview

This chapter covers how the `Agent` tool works, the subagent lifecycle, and built-in subagents (Explore / Plan / General-purpose). Since the subject is Claude Code's automatic subagent selection, this directory provides **minimal demo materials for reproducing the three hands-on examples** from the chapter.

## Files

| File | Purpose |
|------|---------|
| `demo-prompts.md` | Prompts to reproduce Examples 1-3 from Ch3 |
| `sample-codebase/src/middleware/auth.ts` | Auth middleware stub (target for Explore in Example 1) |
| `sample-codebase/src/routes/protected.ts` | Protected endpoint stub |
| `sample-codebase/src/utils/token.ts` | Session verification utility stub |
| `sample-codebase/tests/auth.test.ts` | Auth test stub |

## Quick Start

```bash
cd ch03-subagent-basics/sample-codebase
claude
```

After launching Claude Code, paste the Example 1 prompt from `demo-prompts.md`. Claude Code should delegate investigation to the Explore subagent, discovering and summarizing the four files. The actual subagent invoked depends on the Claude Code version and prompt wording -- check `demo-prompts.md` observation points to verify behavior.

Example 3 (Git worktree isolation) requires a Git repository. Since this companion repo is already Git-managed, just `git clone` and `cd` into `sample-codebase/`. Do not run `git init` inside the companion repo (it would create a nested Git repository).

## About the Sample Files

The TypeScript files under `sample-codebase/` **intentionally omit full type resolution and won't compile**. They're stubs designed for Explore to discover and summarize. They also serve as a starting point for readers to practice JWT refactoring.

## What You'll Learn

- Subagent definitions and independent context windows
- `Agent` tool parameters (`description`, `prompt`, `subagent_type`, `model`, `isolation`, `run_in_background`)
- Foreground vs. background execution modes
- Built-in subagent selection (Explore, Plan, General-purpose)
- Subagent constraints (no nesting, no shared context, no session persistence)
- Subagents vs. agent teams

## Prerequisites

- Claude Code CLI (latest version)
- Git (for Example 3)
