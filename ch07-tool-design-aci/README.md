# Ch07: ツール設計・ACI

書籍「Claude Code マルチエージェント実践ガイド」第7章のサンプルコードです。

## ファイル一覧

| ファイル | 種類 | 説明 |
|---------|------|------|
| `schemas/search-customers.json` | ツールスキーマ | `response_format`による詳細度制御パターン |
| `schemas/search-logs.json` | ツールスキーマ | ページネーション（`limit`/`offset`）パターン |
| `schemas/list-issues.json` | ツールスキーマ | `enum`フィルタリングパターン |
| `schemas/search-knowledge-base.json` | ツールスキーマ | 詳細な`description`記述の実例 |
| `schemas/read-tool.json` | ツールスキーマ | 絶対パス強制パターン（Claude Code実例） |
| `schemas/grep-tool.json` | ツールスキーマ | 出力モード制御パターン（Claude Code実例） |

## 使い方

これらのJSONファイルは、MCPサーバー開発時のツール定義のリファレンスとして参照してください。自作MCPサーバーのツール定義に、各パターンを適用できます。

### パターン別の活用

- **詳細度制御**: `search-customers.json` -- `response_format`パラメータで`concise`/`detailed`を切り替え
- **ページネーション**: `search-logs.json` -- `limit`と`offset`でレスポンス量を制御
- **フィルタリング**: `list-issues.json` -- `enum`で選択肢を限定し、エージェントの判断を支援
- **説明文の書き方**: `search-knowledge-base.json` -- 使用場面・対象外・クエリのヒントを含めた説明
- **パス安全性**: `read-tool.json` -- 絶対パスを強制し、相対パスエラーを防止
- **出力モード**: `grep-tool.json` -- 段階的な情報取得（ファイル一覧→内容確認）を可能にする設計

## 前提条件

- Claude Code CLI（最新版）
- MCPサーバー開発の基礎知識
