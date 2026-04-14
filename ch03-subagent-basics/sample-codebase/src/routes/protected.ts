// protected.ts — Protected endpoints requiring authentication (demo).
// Referenced in Ch3 Example 1 as a consumer of the auth middleware.
import { requireAuth } from "../middleware/auth";
import type { Router } from "./types";

export function registerProtectedRoutes(router: Router): void {
  router.get("/me", requireAuth, (req, res) => {
    res.json({ id: req.user.id });
  });
  router.get("/dashboard", requireAuth, (req, res) => {
    res.json({ widgets: [] });
  });
  router.post("/logout", requireAuth, (_req, res) => {
    res.status(204).end();
  });
}
