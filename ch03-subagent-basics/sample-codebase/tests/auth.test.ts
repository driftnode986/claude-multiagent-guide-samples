// auth.test.ts — Minimal tests for requireAuth middleware (demo, not implemented).
// Stub for Explore subagent to discover in Ch3 Example 1.
import { requireAuth } from "../src/middleware/auth";

describe("requireAuth", () => {
  it("rejects requests without a session cookie", () => {
    // TODO: Add mock request expecting 401 response
  });

  it("attaches user info when the cookie is valid", () => {
    // TODO: Verify req.user.id === 'user-1' with demo-cookie
  });
});
