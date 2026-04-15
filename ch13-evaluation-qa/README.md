# Ch13: Evaluating Agent Performance

Sample code for Chapter 13 of *Multi-Agent Development with Claude Code*.

## Files

| File | Type | Description |
|------|------|-------------|
| `eval-tasks/fix-auth-bypass.yml` | YAML | Evaluation task definition for an auth bypass fix (with pass/fail criteria) |
| `eval-tasks/auth.py` | Python | Code under test (contains an empty-password bypass bug) |
| `eval-tasks/test_empty_pw_rejected.py` | Python | Grader that verifies empty passwords are rejected |
| `eval-tasks/test_null_pw_rejected.py` | Python | Grader that verifies null passwords are rejected |
| `agents/eval-runner.md` | Subagent definition | Agent that executes evaluation tasks and records results |
| `settings-regression-hooks.json` | JSON | `settings.json` config for regression detection hooks |

## Usage

### Defining Evaluation Tasks

Use `eval-tasks/fix-auth-bypass.yml` as a template to create project-specific evaluation tasks. Each task includes:

- `id`: a unique identifier
- `desc`: an unambiguous task description
- `graders`: pass/fail criteria using deterministic tests or state checks

### Running Evaluations

Place `agents/eval-runner.md` in `.claude/agents/` and invoke it as a subagent.

### Regression Detection

Merge `settings-regression-hooks.json` into your `.claude/settings.json` to run the regression suite before every file write or edit. Create `scripts/run-regression-suite.sh` tailored to your project.

## Prerequisites

- Claude Code CLI (latest version)
- A project-specific test suite
