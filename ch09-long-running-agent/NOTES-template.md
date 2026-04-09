# NOTES.md（エージェントが自動生成・更新）

## 現在の作業状況
- 認証モジュールのリファクタリング中
- JWT検証ロジックを auth/jwt.ts に集約する方針

## 発見した問題
- auth/middleware.ts:45 でトークン期限切れの処理が欠落
- tests/auth.test.ts のテストが3件失敗中

## 次のステップ
1. auth/jwt.ts の validateToken を修正
2. テストを全件パスさせる
3. auth/middleware.ts のリファクタリング
