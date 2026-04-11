# Claude Code マルチエージェント実践ガイド — サンプルコード

書籍「Claude Code マルチエージェント実践ガイド」のサンプルコードリポジトリです。

## 構成

| ディレクトリ | 対応章 | 内容 | ファイル数 |
|------------|--------|------|-----------|
| `ch01-why-multiagent/` | Ch1 | なぜマルチエージェントか | 1 |
| `ch02-five-patterns/` | Ch2 | 5つのパターン＋動くサンプル | 4 |
| `ch03-subagent-basics/` | Ch3 | サブエージェント基礎 | 5 |
| `ch04-custom-subagent/` | Ch4 | カスタムサブエージェント作成 | 5 |
| `ch05-subagent-mcp/` | Ch5 | サブエージェント + MCP連携 | 4 |
| `ch06-orchestrator-design/` | Ch6 | オーケストレーター設計 | 2 |
| `ch07-tool-design-aci/` | Ch7 | ツール設計・ACI | 6 |
| `ch08-prompt-principles/` | Ch8 | エージェントプロンプトの8原則 | 7 |
| `ch09-long-running-agent/` | Ch9 | セッションをまたぐ長期エージェント | 7 |
| `ch10-error-recovery/` | Ch10 | エラー回復と失敗モード分類 | 8 |
| `ch11-agent-team-concept/` | Ch11 | エージェントチームの概念と有効化 | 2 |
| `ch12-parallel-development/` | Ch12 | 実践・並列開発 | 4 |
| `ch13-evaluation-qa/` | Ch13 | 評価・品質保証 | 3 |
| `ch14-production-reliability/` | Ch14 | 本番信頼性 | 3 |
| `appendix-a-reference/` | 付録A | コマンド・設定リファレンス | 3 |

## ファイルの種類

| 拡張子 | 配置先 | 説明 |
|--------|--------|------|
| `agents/*.md` | 各章 | カスタムサブエージェント定義（`.claude/agents/` に配置して使用） |
| `*.sh` | 各章 | シェルスクリプト（ハーネス、Hooks、検証） |
| `schemas/*.json` | Ch7 | ツール定義のJSONスキーマ |
| `*.json` | 各章 | Claude Code設定ファイル（`settings.json`等） |
| `*.yml` | 各章 | 戦略定義・タスク定義 |
| `CLAUDE-*.md` | 各章 | CLAUDE.mdテンプレート（プロジェクトルートに配置して使用） |

## クイックスタート

```bash
git clone https://github.com/driftnode986/claude-multiagent-guide-samples.git
cd claude-multiagent-guide-samples
```

### サブエージェントを使う

```bash
# 例: Ch4のテストライターを自分のプロジェクトにコピー
cp ch04-custom-subagent/agents/test-writer.md your-project/.claude/agents/
```

### エージェントチームを有効化する

```bash
# Ch11の設定を参考にsettings.jsonを更新
cat ch11-agent-team-concept/settings-agent-teams.json
```

## 動作環境

- Claude Code CLI（最新版）
- macOS / Linux

## 使い方

各ディレクトリの `README.md` を参照してください。

## 書籍情報

- タイトル: Claude Code マルチエージェント実践ガイド
- 著者: 牧野 誠
