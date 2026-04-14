// token.ts — Session cookie verification utility (demo).
// Referenced in Ch3 Example 1 as the token verification module.
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
