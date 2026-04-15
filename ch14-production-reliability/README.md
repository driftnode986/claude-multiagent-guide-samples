# 第14章: 本番環境での信頼性

「Claude Codeマルチエージェント実践ガイド」第14章のサンプルコードとリファレンス資料です。

## 概要

この章では運用パターンとチェックリストを中心に扱います。サンプルコードはコンクリートなコードで示しやすいコスト閾値アラートの最小実装を提供します。

## ファイル

| ファイル | 説明 |
|---------|------|
| `cost_alert.py` | JSONLログを集計してコスト累計またはターン数上限の超過を検出する |
| `record_turn.sh` | 1ターン分のイベントを `cost-log.jsonl` に追記するシェルヘルパー |
| `sample-events.jsonl` | テスト用のサンプルログ（2セッション・4イベント） |

## クイックスタート

```bash
# サンプルログに対して閾値チェックを実行する（10ドル / 50ターン）
python cost_alert.py --log sample-events.jsonl --max-usd 10 --max-turns 50

# 期待される出力（stderr）
# [OK] sessions=2 total=$0.57 max_turns=3
```

閾値超過をシミュレートする場合:

```bash
# 低い閾値を指定してアラートを発生させる
python cost_alert.py --log sample-events.jsonl --max-usd 0.1 --max-turns 50
# [ALERT] USD>0.10 | sessions=2 total=$0.57 max_turns=3
# (exit 1)
```

無効なモデル名や不正なJSONは終了コード2と `[ERROR]` を出力します。アラートの終了コードと区別することで、ログのバグを早期に発見できます。

新しいターンイベントを追記するには `record_turn.sh` を使います:

```bash
# 使い方: ./record_turn.sh <セッション> <ターン> <モデル> <入力トークン数> <出力トークン数>
COST_LOG=cost-log.jsonl ./record_turn.sh s1 1 sonnet 1200 340
COST_LOG=cost-log.jsonl ./record_turn.sh s1 2 opus 15000 4200
python cost_alert.py --log cost-log.jsonl --max-usd 10 --max-turns 50
```

## ハーネスへの組み込み

第9章のハーネス（または任意のカスタムスクリプト）で各ツール呼び出しの後に `record_turn.sh` を呼び出してください。各セッション終了時に `cost_alert.py` を実行し、終了コードが0以外であれば新しいセッションの開始を停止します。

```bash
# セッション終了フックの例
if ! python cost_alert.py --log cost-log.jsonl --max-usd 10 --max-turns 50; then
  echo "コスト閾値を超過しました。調査後に再開してください。"
  exit 1
fi
```

## 価格テーブルのメンテナンス

`cost_alert.py` 冒頭の `PRICING` ディクショナリにはAnthropicのスタンダードティアの参考価格が記載されています（説明目的のみ）。本番環境で使用する前に https://www.anthropic.com/pricing で最新価格を確認し、ディクショナリを更新してください。新しいモデルや価格変更があった場合、このディクショナリだけを更新すれば済むように設計されています。

## 本章の主要トピック（書籍本文）

| トピック | 内容 |
|---------|------|
| チェックポイント戦略 | 定期的・エラー発生時のチェックポイントによるリカバリー設計 |
| トレースログ構造 | セッション単位のステップ記録（ツール呼び出し・トークン数・所要時間） |
| モデルの階層化 | コスト最適なモデル配置: リード（Opus）・ワーカー（Sonnet）・バリデーター（Haiku） |
| パーミッション階層 | 開発・CI/CD・本番環境向けのパーミッション設計 |
| レインボーデプロイ | 複数バージョンを並行稼働させながら段階的にトラフィックを移行する |
| インシデント対応 | 無限ループ・コスト暴走・品質劣化・カスケード障害の検出と対応フロー |

## 参考資料

- Anthropic Engineering Blog, "How we built our multi-agent research system" (2025-06)
- Anthropic Engineering Blog, "Building a C compiler with a team of parallel Claudes" (2026-02)
- Anthropic 価格ページ: https://www.anthropic.com/pricing

## 動作要件

- Python 3.9以上
- Bash 4以上（`record_turn.sh` の使用に必要）
- Claude Code CLI（最新版）
