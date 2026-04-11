// auth.test.ts — requireAuth ミドルウェアの最小テスト (デモ用、未実装)。
// Ch3 例1 で Explore サブエージェントが拾う "tests/auth.test.ts" のスタブ。
import { requireAuth } from "../src/middleware/auth";

describe("requireAuth", () => {
  it("rejects requests without a session cookie", () => {
    // TODO: モックリクエストで 401 を期待するテストを追加する
  });

  it("attaches user info when the cookie is valid", () => {
    // TODO: demo-cookie で req.user.id === 'user-1' を期待するテストを追加する
  });
});
