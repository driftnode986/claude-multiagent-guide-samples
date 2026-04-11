// protected.ts — 認証必須エンドポイント (デモ用)。
// Ch3 例1 で「protected.ts が 15 ルートで使用」と言及される擬似実装。
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
