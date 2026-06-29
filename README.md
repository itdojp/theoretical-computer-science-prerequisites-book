# 理論計算機科学を読むための数学・証明・アルゴリズム基礎

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-ready-green)](https://itdojp.github.io/theoretical-computer-science-prerequisites-book/)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://github.com/itdojp/it-engineer-knowledge-architecture/blob/main/LICENSE.md)
[![Jekyll](https://img.shields.io/badge/Jekyll-book%20site-blue)](https://jekyllrb.com/)

集合・論理から確率・数論・形式モデルまで。

本書は、既存の『理論計算機科学教科書』を読む前に必要となる前提知識を補強するためのブリッジ教材です。

## 読者向け導線

- 公開サイト: https://itdojp.github.io/theoretical-computer-science-prerequisites-book/
- 本体教科書: https://itdojp.github.io/theoretical-computer-science-textbook/
- リポジトリ: https://github.com/itdojp/theoretical-computer-science-prerequisites-book
- フィードバック: GitHub Issues

## この本の目的

理論計算機科学の本文に入る前に、次の基礎を演習中心で確認します。

- 集合、論理、量化記号
- 関数、関係、同値関係、順序
- 直接証明、対偶証明、背理法、帰納法、構造帰納法
- 漸近記法、総和、再帰式、擬似コード
- グラフ、木、探索、基本データ構造
- 組合せ、数え上げ、形式言語、DFA/NFA の入口
- 確率、期待値、数論、合同算術、線形代数の最小限
- 状態遷移、非決定性、safety/liveness、合意問題の入口

本書単体で理論計算機科学を完結させることは目的としません。到達目標は、定義・定理・証明・擬似コードで止まらずに『理論計算機科学教科書』へ進める状態を作ることです。

## 想定読者

- 理論計算機科学を学びたいが、数学記法・証明・離散数学に不安がある読者
- 実務経験はあるが、集合・論理・計算量・形式言語・確率・数論を体系的に補強したいソフトウェアエンジニア
- 『理論計算機科学教科書』へ入る前に前提診断と演習で準備したい読者
- 研修・輪読会で理論計算機科学の前処理教材を使いたい教員・研修担当者

## 非対象読者

- 競技プログラミングやコーディング面接の短期対策だけを求める読者
- 情報理論、暗号理論、並行計算だけを専門書レベルで深掘りしたい読者
- 機械学習、深層学習、LLM の理論を直接学びたい読者

## 読み方

### 最短ルート

```text
前提診断
  ↓
弱点別リカバリールート
  ↓
必要章だけ読む
  ↓
章末確認チェック
  ↓
本体教科書 readiness checklist
  ↓
理論計算機科学教科書へ
```

### 標準ルート

```text
前提診断
  ↓
Core 第1〜5章
  ↓
Standard 第6〜9章
  ↓
Extended 第10〜13章から必要箇所
  ↓
演習・統合到達確認テスト
  ↓
ミニプロジェクト
  ↓
理論計算機科学教科書へ
```

## 収録範囲

### Part I: Core

- 第1章: 集合と論理
- 第2章: 関数と関係
- 第3章: 証明技法
- 第4章: 漸近記法
- 第5章: 擬似コードと再帰

### Part II: Standard

- 第6章: グラフと木
- 第7章: 組合せと数え上げ
- 第8章: データ構造と基本アルゴリズム
- 第9章: 形式言語の入口

### Part III: Extended

- 第10章: 確率の基礎
- 第11章: 数論・代数の基礎
- 第12章: 線形代数の最小限
- 第13章: 並行性と形式モデルの入口

### 付属資料

- 前提診断 80問
- Core / Standard / Extended 演習と解答
- 追加ドリル
- 章別レビュー問題
- 採点ルーブリック
- 到達判定表
- 弱点別リカバリールート
- 本体教科書 readiness checklist
- 統合到達確認テスト
- 図表
- Python実装ノート
- Python examples
- ミニプロジェクト
- 用語索引・記号索引・概念別逆引き
- 研修・輪読会運用文書

## ローカル確認

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
bundle install
bundle exec jekyll serve --source docs --config docs/_config.yml --destination _site
```

品質チェック:

```bash
python scripts/check_links.py
python scripts/check_exercise_labels.py
python scripts/check_exercise_solution_mapping.py
python examples/python/tests.py
python -m pytest
bundle exec jekyll build --source docs --config docs/_config.yml --destination _site
```

## GitHub Pages

このリポジトリは、他の ITDO 書籍と同じ Jekyll ベースの書籍レイアウトで構成しています。`.github/workflows/pages.yml` により、`main` ブランチへの push で GitHub Pages へデプロイします。

GitHub Pages は **GitHub Actions** からデプロイします。Pages workflow は初回実行時に Pages 設定の有効化も試みます。

## このリポジトリについて

- `docs/`: 本文、演習、図表、評価資料、および GitHub で参照するリポジトリ保守資料
- `examples/python/`: 小規模な Python 実装例
- `scripts/`: 品質チェック・リリース補助スクリプト
- `tests/`: pytest 用テスト
- `.github/workflows/`: CI と Pages デプロイ

書籍サイトでは読者向けの本文・演習・索引を主導線にしています。リリース、監査、保守、テンプレート類は GitHub 上の `docs/audit/`、`docs/release/`、`docs/operations/`、`docs/forms/`、`docs/quality/` を参照してください。

## ライセンス

本書は ITDO Inc. の統一ライセンスに従います。

- ライセンス本文: https://github.com/itdojp/it-engineer-knowledge-architecture/blob/main/LICENSE.md
- クリエイティブ・コモンズ: CC BY-NC-SA 4.0
- 商用利用は別途ライセンス契約が必要です。

第三者教材・外部講義・外部書籍へのリンクや参照は、それぞれの権利者のライセンス・利用条件に従います。

## 連絡先

- 著者: ITDO Inc.（株式会社アイティードゥ）
- Email: knowledge@itdo.jp
- GitHub: https://github.com/itdojp
