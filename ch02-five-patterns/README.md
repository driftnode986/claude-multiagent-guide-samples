# Ch02: Five Workflow Patterns

Companion code for Chapter 2 of *Multi-Agent Development with Claude Code*.

## Files

| File | Type | Description |
|------|------|-------------|
| `prompt-chain.sh` | Shell | Prompt chaining pattern: sequential execution with gates |
| `routing.sh` | Shell | Routing pattern: model selection based on task classification |
| `parallel-review.sh` | Shell | Parallelization pattern: code review across three perspectives |
| `eval-optimize-loop.sh` | Shell | Evaluator-optimizer pattern: iterative improvement loop |

## Usage

Each script runs independently. Execute from the project root directory.

```bash
# Prompt chaining (type check -> add tests)
bash prompt-chain.sh

# Routing (set the USER_QUERY variable before running)
USER_QUERY="Explain how authentication works" bash routing.sh

# Parallel review (reviews the diff between main and HEAD)
bash parallel-review.sh

# Evaluator-optimizer loop (up to 3 improvement cycles)
bash eval-optimize-loop.sh
```

## Prerequisites

- Claude Code CLI (latest version)
- Node.js / npm (`prompt-chain.sh` uses `npx tsc` and `npm test`)
- jq (`routing.sh`, `eval-optimize-loop.sh` use it for JSON parsing)
- Git (`parallel-review.sh` uses `git diff`)
