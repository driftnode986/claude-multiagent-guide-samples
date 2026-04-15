"""Internal Knowledge Base Search MCP Server (Ch07 Sample)

A FastMCP server implementation embodying the 6 ACI principles.
See Chapter 7 of *Multi-Agent Development with Claude Code*.

Tested with: mcp[cli] >= 1.12, Python >= 3.10
Run:
    uv run server.py
Register with Claude Code (match the registration name to the FastMCP name):
    claude mcp add --transport stdio kb -- uv run /path/to/server.py
"""

from typing import Literal

from pydantic import BaseModel, Field

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("kb")

# --- Dataset (replace with a DB / API / vector search in production) ---
ARTICLES: dict[str, dict] = {
    "kb-onboarding-001": {
        "title": "New Member Onboarding Guide",
        "category": "hr",
        "summary": "Day-one through week-one steps and access request workflow",
        "body": "Day 1: PC setup and Slack onboarding. Day 2: VPN request.",
        "updated_at": "2026-03-15",
    },
    "kb-deploy-002": {
        "title": "Production Deploy Approval Flow",
        "category": "engineering",
        "summary": "Steps from staging verification to production release",
        "body": "Production deploys require approval from at least two reviewers.",
        "updated_at": "2026-04-01",
    },
    "kb-incident-003": {
        "title": "Incident Response Playbook",
        "category": "engineering",
        "summary": "First-response actions and contact list for P0/P1 incidents",
        "body": "On a P0 incident, immediately join #incident-war-room.",
        "updated_at": "2026-03-28",
    },
    "kb-expense-004": {
        "title": "Expense Report Submission Guide",
        "category": "finance",
        "summary": "Three-step process from receipt upload to approval",
        "body": "Expenses close at month-end; reimbursement arrives on the 10th.",
        "updated_at": "2026-02-20",
    },
}

Category = Literal["hr", "engineering", "finance", "sales"]
ResponseFormat = Literal["concise", "detailed"]


class ArticleSummary(BaseModel):
    """Minimal article info included in search results."""

    article_id: str = Field(description="Article ID (e.g. kb-deploy-002)")
    title: str = Field(description="Article title")
    category: str = Field(description="Category name")
    updated_at: str = Field(description="Last updated date (YYYY-MM-DD)")


class ArticleDetail(ArticleSummary):
    """Full article fields (detailed mode or single-article fetch)."""

    summary: str = Field(description="One- to two-sentence summary")
    body: str = Field(description="Full body text (Markdown)")


class SearchResult(BaseModel):
    """Top-level structure for search responses."""

    results: list[ArticleSummary | ArticleDetail] = Field(
        description="List of matched articles"
    )
    total_count: int = Field(description="Total matches for the filter criteria")
    showing: int = Field(description="Number of results in this response")
    next_offset: int | None = Field(
        description="Offset for the next page, or null if no more pages"
    )


@mcp.tool()
def search_articles(
    query: str,
    category: Category | None = None,
    response_format: ResponseFormat = "concise",
    limit: int = 20,
    offset: int = 0,
) -> SearchResult:
    """Search the internal knowledge base by keyword.

    Start with a short, broad query, then narrow down based on results.
    Covers: process docs, design docs, runbooks, HR policies.
    Does NOT cover: source code (use the code search tool instead).

    Usage hints:
    - query: one or more keywords separated by spaces
    - category: specify only when narrowing to a specific domain;
      omit to search all categories
    - response_format: use 'concise' first to scan result counts,
      then fetch 'detailed' only for articles of interest — avoid
      requesting 'detailed' for every search
    - limit / offset: page through results until 'next_offset' is null
    """
    if not query.strip():
        raise ValueError(
            "query must not be empty. Provide at least one search keyword."
        )
    if limit < 1 or limit > 100:
        raise ValueError("limit must be between 1 and 100.")
    if offset < 0:
        raise ValueError("offset must be 0 or greater.")

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
    """Retrieve the full text of an article by its ID.

    Typically called after obtaining article_id from search_articles.
    Returns a ValueError with correction hints for unknown IDs.
    """
    if article_id not in ARTICLES:
        examples = ", ".join(list(ARTICLES.keys())[:3])
        raise ValueError(
            f"article_id '{article_id}' does not exist. "
            f"Use search_articles to find the correct ID. "
            f"Examples: {examples}"
        )
    a = ARTICLES[article_id]
    return ArticleDetail(article_id=article_id, **a)


if __name__ == "__main__":
    mcp.run(transport="stdio")
