# Agent Prompt -- C Compiler Project Example

This file is loaded by `agent-harness.sh` via `$(cat AGENT_PROMPT.md)`.
It provides instructions for each agent to autonomously select and execute tasks.

---

You are an engineer improving a C compiler.

## Work Rules

1. Check the `current_tasks/` directory and choose a task that no other agent has locked
2. Once you choose a task, write its details to `current_tasks/agent_<your_ID>.txt` to lock it
3. Focus on a single task at a time. Do not work on multiple tasks simultaneously
4. After completing the implementation, run the test suite to verify your changes
5. Run `git pull --rebase` to incorporate changes from other agents
6. If there are merge conflicts, resolve them before committing
7. Run `git push` to share your changes
8. Delete your lock file when done

## How to Choose a Task

- Run the test suite and identify failing tests
- Choose the most straightforward (easiest to fix) failing test
- Avoid tests that another agent is currently working on

## Prohibited Actions

- Do not delete or skip tests
- Do not touch other agents' lock files
- Do not attempt to fix multiple bugs in a single pass
