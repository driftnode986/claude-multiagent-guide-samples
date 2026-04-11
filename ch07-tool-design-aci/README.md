# Ch07: ツール設計・ACI

書籍「Claude Code マルチエージェント実践ガイド」第7章のサンプルコードです。

## ファイル一覧

### 動く MCP サーバー実装

| ファイル | 種類 | 説明 |
|---------|------|------|
| `server.py` | FastMCP サーバー | ACI 6 原則を体現する社内ナレッジベース検索サーバー（約170行） |
| `pyproject.toml` | プロジェクト定義 | `mcp[cli]` と `pydantic` の依存定義 |

### ツールスキーマ参考例

| ファイル | 種類 | 説明 |
|---------|------|------|
| `schemas/search-customers.json` | ツールスキーマ | `response_format`による詳細度制御パターン |
| `schemas/search-logs.json` | ツールスキーマ | ページネーション（`limit`/`offset`）パターン |
| `schemas/list-issues.json` | ツールスキーマ | `enum`フィルタリングパターン |
| `schemas/search-knowledge-base.json` | ツールスキーマ | 詳細な`description`記述の実例 |
| `schemas/read-tool.json` | ツールスキーマ | 絶対パス強制パターン（Claude Code実例） |
| `schemas/grep-tool.json` | ツールスキーマ | 出力モード制御パターン（Claude Code実例） |

## クイックスタート（server.py を動かす）

### 1. インストール

```bash
cd ch07-tool-design-aci
uv sync
```

または `uv` を使わない場合:

```bash
pip install "mcp[cli]>=1.12" "pydantic>=2.0"
```

### 2. Claude Code に登録

```bash
claude mcp add --transport stdio kb -- uv run /absolute/path/to/server.py
```

`/absolute/path/to/server.py` は環境に合わせて実パスに置き換えてください。
登録後、Claude Code 起動中に `/mcp` で `kb` サーバーの状態を確認できます。

### 3. 動作確認

Claude Code セッションで以下のように質問すると、`kb__search_articles` ツールが
呼ばれます。

```text
社内のオンボーディング手順を教えて
```

最初は `concise` モードで件数だけ返り、注目した記事を `kb__get_article_detail`
または `response_format=detailed` で深掘りする想定です。

## ACI 6 原則と server.py の対応

| 原則 | server.py での体現箇所 |
|------|----------------------|
| 1. 適切なツールを選ぶ | 全件取得 `list_articles` を作らず、`search_articles` のみ提供 |
| 2. ツールを統合する | カテゴリ・キーワード・ページネーションを 1 ツールに集約 |
| 3. 名前空間で境界を明確にする | `claude mcp add` の登録名 `kb` → `mcp__kb__search_articles` |
| 4. 意味のあるコンテキストを返す | UUID ではなく `kb-deploy-002` 形式の人間可読な ID |
| 5. トークン効率を最適化する | `response_format` (concise/detailed) と `limit/offset` |
| 6. ツール説明をプロンプトエンジニアリング | docstring に使用場面・対象外・ヒントを記述 |

## ツールスキーマ参考例の活用

`schemas/` ディレクトリの JSON ファイルは、自作 MCP サーバーのツール定義リファレンス
として参照してください。各パターンは server.py 内の対応箇所と一緒に確認できます。

- **詳細度制御**: `search-customers.json` ↔ `server.py` の `response_format`
- **ページネーション**: `search-logs.json` ↔ `server.py` の `limit`/`offset`
- **フィルタリング**: `list-issues.json` ↔ `server.py` の `category`
- **説明文の書き方**: `search-knowledge-base.json` ↔ `server.py` の docstring
- **パス安全性**: `read-tool.json` -- Claude Code 実例
- **出力モード**: `grep-tool.json` -- Claude Code 実例

## 前提条件

- Claude Code CLI（最新版）
- Python 3.10 以上
- `mcp[cli]` 1.12 以上
