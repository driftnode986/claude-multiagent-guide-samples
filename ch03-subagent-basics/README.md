# 第3章: サブエージェントの仕組み

「Claude Codeマルチエージェント実践ガイド」第3章のサンプルコードです。

## 概要

この章では、`Agent` ツールの動作原理、サブエージェントのライフサイクル、および組み込みサブエージェント（Explore / Plan / 汎用）を扱います。テーマはClaude Codeによるサブエージェントの自動選択であるため、このディレクトリは**本章の3つのハンズオン例を再現するための最小限のデモ素材**を提供します。

## ファイル

| ファイル | 用途 |
|---------|------|
| `demo-prompts.md` | 第3章の例1〜3を再現するためのプロンプト |
| `sample-codebase/src/middleware/auth.ts` | 認証ミドルウェアのスタブ（例1のExploreの対象） |
| `sample-codebase/src/routes/protected.ts` | 保護されたエンドポイントのスタブ |
| `sample-codebase/src/utils/token.ts` | セッション検証ユーティリティのスタブ |
| `sample-codebase/tests/auth.test.ts` | 認証テストのスタブ |

## クイックスタート

```bash
cd ch03-subagent-basics/sample-codebase
claude
```

Claude Codeを起動したら、`demo-prompts.md` の例1のプロンプトを貼り付けてください。Claude CodeがExploreサブエージェントに調査を委譲し、4つのファイルを発見・要約するはずです。実際に呼び出されるサブエージェントはClaude Codeのバージョンとプロンプトの文言によって異なります。動作を確認するには `demo-prompts.md` の観察ポイントを参照してください。

例3（Gitワークツリーの分離）はGitリポジトリが必要です。このリポジトリはすでにGit管理されているので、`git clone` して `sample-codebase/` に `cd` するだけで使えます。リポジトリ内で `git init` を実行しないでください（ネストしたGitリポジトリが作成されてしまいます）。

## サンプルファイルについて

`sample-codebase/` 以下のTypeScriptファイルは**意図的に型解決を省略しており、コンパイルできません**。Exploreが発見・要約するためのスタブです。また、読者がJWTリファクタリングを練習するための出発点としても利用できます。

## 学習内容

- サブエージェントの定義と独立したコンテキストウィンドウ
- `Agent` ツールのパラメータ（`description`、`prompt`、`subagent_type`、`model`、`isolation`、`run_in_background`）
- フォアグラウンドとバックグラウンドの実行モード
- 組み込みサブエージェントの選択（Explore、Plan、汎用）
- サブエージェントの制約（ネスト不可、コンテキスト非共有、セッション非永続）
- サブエージェントとエージェントチームの違い

## 動作要件

- Claude Code CLI（最新版）
- Git（例3で使用）
