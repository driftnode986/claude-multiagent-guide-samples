# Claude Codeマルチエージェント実践ガイド — サンプルコード

書籍「Claude Codeマルチエージェント実践ガイド」のサンプルコードリポジトリです。

## ディレクトリ構成

| ディレクトリ | 章 | 内容 | ファイル数 |
|-------------|-----|------|-----------|
| `ch01-why-multiagent/` | 第1章 | マルチエージェントが必要な理由 | 2 |
| `ch02-five-patterns/` | 第2章 | 5つのワークフローパターン | 4 |
| `ch03-subagent-basics/` | 第3章 | サブエージェントの仕組み | 5 |
| `ch04-custom-subagent/` | 第4章 | カスタムサブエージェントの構築 | 5 |
| `ch05-subagent-mcp/` | 第5章 | MCPでサブエージェントを外部ツールと接続する | 4 |
| `ch06-orchestrator-design/` | 第6章 | オーケストレーターの設計 | 2 |
| `ch07-tool-design-aci/` | 第7章 | エージェント向けツールの設計 | 6 |
| `ch08-prompt-principles/` | 第8章 | 効果的なエージェントプロンプトの書き方 | 7 |
| `ch09-long-running-agent/` | 第9章 | 長時間エージェントセッションの管理 | 7 |
| `ch10-error-recovery/` | 第10章 | エラーリカバリーと障害モード | 8 |
| `ch11-agent-team-concept/` | 第11章 | エージェントチームの始め方 | 2 |
| `ch12-parallel-development/` | 第12章 | エージェントチームの実践 | 4 |
| `ch13-evaluation-qa/` | 第13章 | エージェントのパフォーマンス評価 | 3 |
| `ch14-production-reliability/` | 第14章 | 本番環境での信頼性 | 3 |
| `appendix-a-reference/` | 付録A | クイックリファレンス | 3 |

## ファイル種別

| 拡張子 | 場所 | 説明 |
|--------|------|------|
| `agents/*.md` | 各章 | カスタムサブエージェント定義（使用するには `.claude/agents/` に配置） |
| `*.sh` | 各章 | シェルスクリプト（ハーネス、フック、バリデーション） |
| `schemas/*.json` | 第7章 | ツール定義JSONスキーマ |
| `*.json` | 各章 | Claude Code設定ファイル（`settings.json` など） |
| `*.yml` | 各章 | 戦略・タスク定義ファイル |
| `CLAUDE-*.md` | 各章 | `CLAUDE.md` テンプレート（プロジェクトルートに配置して使用） |

## クイックスタート

```bash
git clone https://github.com/driftnode986/claude-multiagent-guide-samples.git
cd claude-multiagent-guide-samples
```

### サブエージェントを使う

```bash
# 例: 第4章のテストライターをプロジェクトにコピーする
cp ch04-custom-subagent/agents/test-writer.md your-project/.claude/agents/
```

### エージェントチームを有効にする

```bash
# 第11章の設定を確認して、自分の settings.json に反映する
cat ch11-agent-team-concept/settings-agent-teams.json
```

## 動作要件

- Claude Code CLI（最新版）
- macOS / Linux

## 使い方

各ディレクトリの `README.md` に章ごとの詳細な手順が記載されています。

## 書籍情報

- **タイトル**: Claude Codeマルチエージェント実践ガイド
- **著者**: 牧野 誠
