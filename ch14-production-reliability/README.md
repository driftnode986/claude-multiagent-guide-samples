# Ch14: 本番信頼性

書籍「Claude Code マルチエージェント実践ガイド」第14章の解説とサンプルコードです。

## 概要

本章は運用パターンとチェックリストが中心ですが、もっとも実装に踏み込めるトピックである「コスト閾値アラート」について最小実装を提供しています。

## ファイル一覧

| ファイル | 役割 |
|---------|------|
| `cost_alert.py` | JSONL ログを集計し、累積コスト・最大ターン数の閾値超過を検出する |
| `record_turn.sh` | 1ターン分のイベントを `cost-log.jsonl` に追記するシェルヘルパー |
| `sample-events.jsonl` | 動作確認用のサンプルログ（4イベント / 2セッション） |

## クイックスタート

```bash
# サンプルログに対して閾値判定を実行 (10 USD / 50 turns)
python cost_alert.py --log sample-events.jsonl --max-usd 10 --max-turns 50

# 期待される出力 (stderr)
# [OK] sessions=2 total=$0.57 max_turns=3
```

閾値超過のシミュレーションは以下のように行います。

```bash
# わずかな閾値で実行するとアラートに切り替わる
python cost_alert.py --log sample-events.jsonl --max-usd 0.1 --max-turns 50
# [ALERT] USD>0.10 | sessions=2 total=$0.57 max_turns=3
# (exit 1)
```

不正なモデル名や壊れた JSON が混入していた場合は exit 2 で `[ERROR]` を返します。ログ書き込み側のバグを早期検出できるよう、アラートと区別された終了コードにしています。

新しいターンを追記するには `record_turn.sh` を使います。

```bash
# usage: ./record_turn.sh <session> <turn> <model> <in_tokens> <out_tokens>
COST_LOG=cost-log.jsonl ./record_turn.sh s1 1 sonnet 1200 340
COST_LOG=cost-log.jsonl ./record_turn.sh s1 2 opus 15000 4200
python cost_alert.py --log cost-log.jsonl --max-usd 10 --max-turns 50
```

## ハーネスへの組み込み方

書籍 Ch9 で構築したハーネスや任意のスクリプトから、ツール呼び出しごとに `record_turn.sh` を呼び出してログを溜めます。1セッションの終わりに `cost_alert.py` を実行し、終了コードが非ゼロなら新規セッションの開始を抑止します。

```bash
# セッション終了時のフック例
if ! python cost_alert.py --log cost-log.jsonl --max-usd 10 --max-turns 50; then
  echo "コスト閾値を超過しました。原因を調査してください。"
  exit 1
fi
```

## 価格表の保守

`cost_alert.py` 冒頭の `PRICING` 辞書は Anthropic Standard tier の参考価格 (例示用) です。本番投入前に <https://www.anthropic.com/pricing> で最新値を確認して上書きしてください。新モデルや価格改定があっても、修正箇所は辞書1箇所だけで済みます。

## 主なトピック（書籍本文）

| トピック | 内容 |
|---------|------|
| チェックポイント戦略 | 定期・エラー時のチェックポイントによる回復設計 |
| トレースログ構造 | セッション単位のステップ記録（ツール呼び出し・トークン・所要時間） |
| モデル階層化 | リード（Opus）・ワーカー（Sonnet）・検証（Haiku）のコスト最適配置 |
| パーミッション階層 | 開発・CI/CD・本番環境ごとのパーミッション設計 |
| レインボーデプロイメント | 複数バージョンの同時実行と段階的トラフィック移行 |
| インシデント対応 | 無限ループ・コスト暴走・品質劣化・カスケード障害の検知と対処フロー |

## 参考

- Anthropic Engineering Blog「How we built our multi-agent research system」（2025-06）
- Anthropic Engineering Blog「Building a C compiler with a team of parallel Claudes」（2026-02）
- Anthropic 価格ページ <https://www.anthropic.com/pricing>

## 前提条件

- Python 3.9 以上
- Bash 4 以上（`record_turn.sh` の利用時）
- Claude Code CLI（最新版）
