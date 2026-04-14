## Multi-Agent Policy

Delegate the following tasks to the corresponding subagent:

- Code review -> code-reviewer subagent
- Test creation -> test-writer subagent
- Documentation updates -> doc-generator subagent

When multiple subagents are needed, delegate independent tasks
in parallel (run_in_background: true).
