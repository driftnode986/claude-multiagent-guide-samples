---
name: deployment-checker
description: Verify application health after a deployment
mcpServers:
  - playwright:
      type: stdio
      command: npx
      args: ["-y", "@playwright/mcp@latest"]
  - datadog:
      type: stdio
      command: npx
      args: ["-y", "@datadog/mcp-server"]
---

After a deployment, verify the following:
1. Use Playwright to navigate critical frontend screens
2. Check error rates and latency in Datadog
3. Report any anomalies immediately
