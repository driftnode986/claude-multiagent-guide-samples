# Ch03 デモプロンプト集

書籍 Ch3 で示した3つの実践例を、自分の手で再現するためのプロンプト集です。`sample-codebase/` を Claude Code から開いて以下を試してみてください。

```bash
cd ch03-subagent-basics/sample-codebase
claude
```

各プロンプトでは、Claude Code が組み込みサブエージェントを自動的に呼び出すかどうかを観察するのが目的です。実際のサブエージェント呼び出しはセッションログ (`/transcript`) や Hooks で確認できます。

## 例1: コードベース調査の委譲 (Explore が自動選択される想定)

```text
このプロジェクトの認証関連ファイルを特定して、各ファイルでどのように認証が
使われているかを要約してください。
```

**観察ポイント**:

- Claude Code が Explore サブエージェントに調査を委譲する
- メインセッションの context は要約結果のみで満たされる
- Explore は読み取り専用なので、ファイルが書き換わらない

**期待される結果**: `src/middleware/auth.ts`, `src/routes/protected.ts`, `src/utils/token.ts`, `tests/auth.test.ts` の4ファイルが特定され、それぞれの役割が短くまとめられる。

## 例2: 並列レビュー (汎用サブエージェントが複数バックグラウンド起動される想定)

`sample-codebase/` に擬似的な PR 差分を想定して以下を投げます。

```text
src/middleware/auth.ts と src/utils/token.ts のセキュリティ・パフォーマンス・
コーディング規約の3観点を、それぞれ別のサブエージェントに並列でレビュー
させてください。最後に統一レポートにまとめてください。
```

**観察ポイント**:

- Claude Code が3つの汎用サブエージェントを `run_in_background: true` で同時起動する
- 各サブエージェントが独立したコンテキストで分析する
- メインエージェントが3つの結果を統合する

**期待される結果**: セキュリティ (例: ハードコードされた `demo-cookie`)、パフォーマンス (例: O(1) lookup の妥当性)、規約 (例: 命名・型定義) の3観点が分けて報告される。

## 例3: Git worktree による隔離実行 (isolation: worktree)

worktree 機能は git リポジトリ内でしか動かないため、本サンプルを使う場合は companion repo 自体を clone して、その中で Claude Code を起動してください。

```bash
git clone https://github.com/driftnode986/claude-multiagent-guide-samples.git
cd claude-multiagent-guide-samples/ch03-subagent-basics/sample-codebase
claude
```

別の場所に切り出して試したい場合は、コピー先で改めて `git init` してください (companion repo の中で `git init` するとネストした git リポジトリになってしまうため)。

```text
auth.ts に対して、JWT ベースの実装に置き換える実験を Git worktree 経由で
試してください。元のワークツリーには影響を与えないでください。
```

**観察ポイント**:

- Claude Code が `isolation: "worktree"` でサブエージェントを起動する
- 一時的な worktree が作成され、メインのワークツリーは変更されない
- 成功すれば worktree のパスとブランチ名が返される

**期待される結果**: 元の `auth.ts` は変更されず、新しいブランチに JWT 実装の試案が乗る。

## 注意事項

- これらのサンプルファイルは TypeScript の型解決を意図的に省略しており、コンパイルは通りません。あくまで Explore がファイルを発見しやすくするためのスタブです。
- どのサブエージェントが起動されるかは Claude Code のバージョンと自動選択ロジックによって変動します。プロンプトの言い回しを変えると別のサブエージェントが選ばれることもあります。
- 例2 と 例3 は「Claude Code がそう判断する可能性が高い」想定であり、必ずバックグラウンド起動・worktree 隔離されるとは限りません。Hooks やトランスクリプトで実際の動作を確認してください。
