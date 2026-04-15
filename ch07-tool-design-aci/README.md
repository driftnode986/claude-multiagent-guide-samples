# 第7章: エージェント向けツールの設計とACI

「Claude Codeマルチエージェント実践ガイド」第7章のサンプルコードです。

## ファイル

### 動作するMCPサーバーの実装

| ファイル | 種別 | 説明 |
|---------|------|------|
| `server.py` | FastMCPサーバー | ACI 6原則を体現した社内ナレッジベース検索サーバー（約170行） |
| `pyproject.toml` | プロジェクト設定 | `mcp[cli]` と `pydantic` の依存関係定義 |

### ツールスキーマのリファレンス例

| ファイル | 種別 | 説明 |
|---------|------|------|
| `schemas/search-customers.json` | ツールスキーマ | `response_format` による冗長性制御パターン |
| `schemas/search-logs.json` | ツールスキーマ | ページネーション（`limit`/`offset`）パターン |
| `schemas/list-issues.json` | ツールスキーマ | `enum` によるフィルタリングパターン |
| `schemas/search-knowledge-base.json` | ツールスキーマ | 詳細な `description` の書き方の例 |
| `schemas/read-tool.json` | ツールスキーマ | 絶対パス強制パターン（Claude Code組み込みの例） |
| `schemas/grep-tool.json` | ツールスキーマ | 出力モード制御パターン（Claude Code組み込みの例） |

## クイックスタート（server.py の実行）

### 1. インストール

```bash
cd ch07-tool-design-aci
uv sync
```

`uv` を使わない場合:

```bash
pip install "mcp[cli]>=1.12" "pydantic>=2.0"
```

### 2. Claude Codeへの登録

```bash
claude mcp add kb --transport stdio -- uv run /absolute/path/to/server.py
```

`/absolute/path/to/server.py` は実際のパスに置き換えてください。
登録後、Claude Code内で `/mcp` を実行して `kb` サーバーのステータスを確認します。

### 3. 動作確認

Claude Codeのセッション内で次のように質問してみてください。

```text
オンボーディング手順を教えてください
```

最初に `mcp__kb__search_articles` ツールが `concise` モードで実行され、記事件数だけが返されます。`mcp__kb__get_article_detail` を呼ぶか、`response_format=detailed` で再検索すると詳細を確認できます。

## ACI 6原則と server.py の対応

| 原則 | server.py での実装方法 |
|------|----------------------|
| 1. 適切なツールを選ぶ | `list_articles` の全件返却なし — フィルタリング付き `search_articles` のみ |
| 2. 機能を集約する | カテゴリ・キーワード・ページネーションを1つのツールに統合 |
| 3. 明確な境界でネームスペースを設ける | `kb` として登録 → ツールは `mcp__kb__search_articles` として表示 |
| 4. 意味のあるコンテキストを返す | UUIDではなく `kb-deploy-002` のような人間が読めるID |
| 5. トークン効率を最適化する | `response_format`（concise/detailed）と `limit`/`offset` |
| 6. ツールの説明をプロンプトエンジニアリングする | docstringにユースケース・除外条件・ヒントを記載 |

## ツールスキーマリファレンスの使い方

`schemas/` 内のJSONファイルは、独自MCPサーバーのツール定義を設計する際のリファレンスパターンとして使います。各パターンは server.py の対応する箇所と対応しています。

- **冗長性制御**: `search-customers.json` ↔ server.py の `response_format`
- **ページネーション**: `search-logs.json` ↔ server.py の `limit`/`offset`
- **フィルタリング**: `list-issues.json` ↔ server.py の `category`
- **説明の書き方**: `search-knowledge-base.json` ↔ server.py の docstring
- **パスの安全性**: `read-tool.json` — Claude Code組み込みの例
- **出力モード**: `grep-tool.json` — Claude Code組み込みの例

## 動作要件

- Claude Code CLI（最新版）
- Python 3.10以上
- `mcp[cli]` 1.12以上
