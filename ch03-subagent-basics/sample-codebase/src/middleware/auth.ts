// auth.ts — セッション Cookie ベースの最小認証ミドルウェア (デモ用)。
// Ch3 例1「認証ミドルウェアを JWT 方式に変更してください」のターゲット。
import type { Request, Response, NextFunction } from "./types";
import { verifySessionCookie } from "../utils/token";

export function requireAuth(
  req: Request,
  res: Response,
  next: NextFunction
): void {
  const cookie = req.headers["cookie"] ?? "";
  const session = verifySessionCookie(cookie);
  if (session === null) {
    res.status(401).send("unauthorized");
    return;
  }
  req.user = { id: session.userId };
  next();
}
