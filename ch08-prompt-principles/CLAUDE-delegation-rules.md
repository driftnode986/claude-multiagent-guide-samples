## Delegation Rules for Subagents

When delegating to subagents, follow this template:

### Required Information
1. **Goal**: State concretely in 1-2 sentences (e.g., "Scan the auth module for SQL injection vulnerabilities")
2. **Output format**: Structure of the result (e.g., "JSON with vulnerability type, file, line number, and severity")
3. **Tool guidance**: Which tools and resources to use (e.g., "Search source code with Grep, then verify files with Read")
4. **Boundaries**: What is out of scope (e.g., "Detection and reporting only — do not apply fixes")

### Prohibited
- Vague instructions like "investigate this"
- Listing file paths without context
- Delegating without specifying the output format
