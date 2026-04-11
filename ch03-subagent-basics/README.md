# Ch03: サブエージェント基礎

書籍「Claude Code マルチエージェント実践ガイド」第3章のサンプルコードです。

## 概要

本章は `Agent` ツールの仕組み、サブエージェントのライフサイクル、組み込みサブエージェント (Explore / Plan / General-purpose) の解説が中心です。動かす対象が「Claude Code 自身による自動選択」のため、本ディレクトリには **書籍の3つの実践例を再現するための最小デモ材料** だけを置いています。

## ファイル一覧

| ファイル | 役割 |
|---------|------|
| `demo-prompts.md` | 書籍 Ch3 の例1〜例3 を自分の手で再現するためのプロンプト集 |
| `sample-codebase/src/middleware/auth.ts` | 認証ミドルウェアのスタブ (例1 で Explore が拾う対象) |
| `sample-codebase/src/routes/protected.ts` | 認証必須エンドポイントのスタブ |
| `sample-codebase/src/utils/token.ts` | セッション検証ユーティリティのスタブ |
| `sample-codebase/tests/auth.test.ts` | 認証テストのスタブ |

## クイックスタート

```bash
cd ch03-subagent-basics/sample-codebase
claude
```

Claude Code を起動したら `demo-prompts.md` の例1のプロンプトをそのまま貼り付けてください。Claude Code が Explore サブエージェントを自動的に呼び出し、4つのファイルを発見・要約する様子が観察できます。

例3 (Git worktree 隔離) を試す場合は、先に `sample-codebase/` を git リポジトリにしておく必要があります。

```bash
cd ch03-subagent-basics/sample-codebase
git init && git add . && git commit -m "initial"
```

## サンプルファイルの位置づけ

`sample-codebase/` 配下の TypeScript ファイルは **TypeScript の型解決を意図的に省略しており、コンパイルは通りません**。あくまで Explore サブエージェントがファイルを発見しやすくするための擬似コードです。読者が JWT 化リファクタリングの題材として手を入れる土台としても使えます。

## 本章で学ぶこと

- サブエージェントの定義と独立コンテキストの仕組み
- `Agent` ツールのパラメータ (`description`, `prompt`, `subagent_type`, `model`, `isolation`, `run_in_background`)
- フォアグラウンド / バックグラウンド実行モード
- 組み込みサブエージェント3種 (Explore, Plan, General-purpose) の使い分け
- サブエージェントの制約 (ネスト不可、コンテキスト非共有、セッション非永続)
- サブエージェントとエージェントチームの違い

## 前提条件

- Claude Code CLI (最新版)
- git (例3 を試す場合)
