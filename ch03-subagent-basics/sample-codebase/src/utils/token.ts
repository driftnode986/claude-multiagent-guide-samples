// token.ts — セッションクッキー検証ユーティリティ (デモ用)。
// Ch3 例1 で「token.ts にトークン検証」と言及される擬似実装。
export type Session = { userId: string; expiresAt: number };

const SESSIONS: Record<string, Session> = {
  "demo-cookie": { userId: "user-1", expiresAt: 9999999999 },
};

export function verifySessionCookie(cookieHeader: string): Session | null {
  const match = cookieHeader.match(/session=([^;]+)/);
  if (match === null) {
    return null;
  }
  const session = SESSIONS[match[1]];
  if (session === undefined || session.expiresAt < Date.now() / 1000) {
    return null;
  }
  return session;
}
