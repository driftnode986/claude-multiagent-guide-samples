"""社内ナレッジベース検索 MCP サーバー（Ch7 サンプル）

ACI 6 原則を体現する FastMCP サーバー実装。
書籍「Claude Code マルチエージェント実践ガイド」第7章 参照。

検証環境: mcp[cli] >= 1.12, Python >= 3.10
起動方法:
    uv run server.py
Claude Code への登録（登録名 kb と FastMCP 内部名を一致させる）:
    claude mcp add --transport stdio kb -- uv run /path/to/server.py
"""

from typing import Literal

from pydantic import BaseModel, Field

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("kb")

# --- データセット（本番では DB / API / ベクトル検索に置き換える） ---
ARTICLES: dict[str, dict] = {
    "kb-onboarding-001": {
        "title": "新メンバー向けオンボーディングガイド",
        "category": "hr",
        "summary": "入社初日から1週間の手順とアクセス申請の流れ",
        "body": "1日目: PCセットアップとSlack参加。2日目: VPN申請。",
        "updated_at": "2026-03-15",
    },
    "kb-deploy-002": {
        "title": "本番デプロイの承認フロー",
        "category": "engineering",
        "summary": "ステージング検証から本番リリースまでの手順",
        "body": "本番デプロイには2名以上のレビューが必要です。",
        "updated_at": "2026-04-01",
    },
    "kb-incident-003": {
        "title": "インシデント対応プレイブック",
        "category": "engineering",
        "summary": "P0/P1 インシデント発生時の初動と連絡先",
        "body": "P0 が発生したら即座に #incident-war-room へ。",
        "updated_at": "2026-03-28",
    },
    "kb-expense-004": {
        "title": "経費精算の申請方法",
        "category": "finance",
        "summary": "領収書のアップロードから承認までの3ステップ",
        "body": "経費は月末締め翌月10日払いです。",
        "updated_at": "2026-02-20",
    },
}

Category = Literal["hr", "engineering", "finance", "sales"]
ResponseFormat = Literal["concise", "detailed"]


class ArticleSummary(BaseModel):
    """検索結果に含める最小限の記事情報。"""

    article_id: str = Field(description="記事ID（例: kb-deploy-002）")
    title: str = Field(description="記事タイトル")
    category: str = Field(description="カテゴリ名")
    updated_at: str = Field(description="最終更新日 YYYY-MM-DD")


class ArticleDetail(ArticleSummary):
    """記事の全フィールド（detailed モードまたは詳細取得時）。"""

    summary: str = Field(description="1〜2文の要約")
    body: str = Field(description="本文（マークダウン）")


class SearchResult(BaseModel):
    """検索レスポンスのトップレベル構造。"""

    results: list[ArticleSummary | ArticleDetail] = Field(
        description="マッチした記事の一覧"
    )
    total_count: int = Field(description="フィルタ条件に合う総件数")
    showing: int = Field(description="このレスポンスで返した件数")
    next_offset: int | None = Field(
        description="次ページがある場合の offset、なければ null"
    )


@mcp.tool()
def search_articles(
    query: str,
    category: Category | None = None,
    response_format: ResponseFormat = "concise",
    limit: int = 20,
    offset: int = 0,
) -> SearchResult:
    """社内ナレッジベースをキーワードで検索します。

    最初は短く広いクエリから始め、結果に応じて絞り込んでください。
    検索対象: 業務手順書、設計書、運用ルール、HR ポリシー。
    検索対象外: ソースコード（コード検索には別ツールを使ってください）。

    使い方のヒント:
    - query: 日本語で入力。空白区切りで複数語を指定できます
    - category: 領域に絞り込みたいときのみ指定。未指定で全カテゴリ
    - response_format: 初回は 'concise' で件数を確認し、注目する記事のみ
      'detailed' で本文を取得してください。常に 'detailed' は避けること
    - limit / offset: 'next_offset' が null になるまで繰り返し取得できます
    """
    if not query.strip():
        raise ValueError(
            "query は空にできません。検索キーワードを1語以上入力してください"
        )
    if limit < 1 or limit > 100:
        raise ValueError("limit は 1〜100 の範囲で指定してください")
    if offset < 0:
        raise ValueError("offset は 0 以上で指定してください")

    terms = query.lower().split()
    matches = [
        (aid, a)
        for aid, a in ARTICLES.items()
        if (category is None or a["category"] == category)
        and all(
            t in a["title"].lower()
            or t in a["summary"].lower()
            or t in a["body"].lower()
            for t in terms
        )
    ]
    total = len(matches)
    page = matches[offset : offset + limit]

    items: list[ArticleSummary | ArticleDetail] = []
    for aid, a in page:
        if response_format == "detailed":
            items.append(ArticleDetail(article_id=aid, **a))
        else:
            items.append(
                ArticleSummary(
                    article_id=aid,
                    title=a["title"],
                    category=a["category"],
                    updated_at=a["updated_at"],
                )
            )

    next_offset = offset + limit if offset + limit < total else None
    return SearchResult(
        results=items,
        total_count=total,
        showing=len(items),
        next_offset=next_offset,
    )


@mcp.tool()
def get_article_detail(article_id: str) -> ArticleDetail:
    """指定した記事IDの全文を取得します。

    通常は search_articles で article_id を取得してから呼び出します。
    存在しない ID の場合は ValueError を返し、修正方法を含めます。
    """
    if article_id not in ARTICLES:
        examples = ", ".join(list(ARTICLES.keys())[:3])
        raise ValueError(
            f"article_id '{article_id}' は存在しません。"
            f"search_articles で正しい ID を取得してください。"
            f"例: {examples}"
        )
    a = ARTICLES[article_id]
    return ArticleDetail(article_id=article_id, **a)


if __name__ == "__main__":
    mcp.run(transport="stdio")
