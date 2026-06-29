# 学習ルート

## 基本方針

この教材は、全員が全章を同じ順序で読むための教材ではない。前提診断で弱点を特定し、必要な章だけを重点的に読む。

## 標準ワークフロー

```text
前提診断
  ↓
採点ルーブリック
  ↓
弱点別リカバリールート
  ↓
該当章を読む
  ↓
図表で直観を確認
  ↓
Python examples で小さい入力を動かす
  ↓
章末確認チェック
  ↓
演習
  ↓
統合到達確認テスト
  ↓
ミニプロジェクト
  ↓
本体教科書 readiness checklist
```

## 得点別ルート

| 前提診断の正答率 | 推奨ルート |
|---:|---|
| 80%以上 | 本体教科書へ進み、詰まった章だけ戻る |
| 60〜79% | Core を確認し、Standard/Extended は失点領域だけ読む |
| 40〜59% | Core + Standard を一通り通す |
| 40%未満 | Core を丁寧に通し、演習を解いてから Standard へ進む |

## Core ルート

対象:

- 集合・論理の記号が不安定
- 証明をどう書けばよいか分からない
- O記法を感覚でしか理解していない
- 再帰・擬似コードを追うのが遅い

読む章:

1. 第1章 集合と論理
2. 第2章 関数と関係
3. 第3章 証明技法
4. 第4章 漸近記法
5. 第5章 擬似コードと再帰

補助:

- 図表: 証明・漸近記法・再帰
- Python: 再帰トレース
- 演習: Core 演習、証明ドリル、漸近記法ドリル、擬似コード・再帰ドリル

## Standard ルート

対象:

- グラフ・木・探索が弱い
- 組合せや場合数の見積もりが弱い
- 基本データ構造の操作と計算量が不安定
- DFA/NFA、文法、文字列言語の記法に慣れていない

読む章:

1. 第6章 グラフと木
2. 第7章 組合せと数え上げ
3. 第8章 データ構造と基本アルゴリズム
4. 第9章 形式言語の入口

補助:

- 図表: BFS、Union-Find、DFA、NFA
- Python: BFS、Union-Find、DFAシミュレータ
- 演習: Standard 演習
- プロジェクト: P2 BFS、P3 Union-Find、P4 DFA

## Extended ルート

対象:

- 情報理論、暗号、線形符号、並行計算へ進む予定がある
- 確率、剰余計算、線形代数、状態遷移の記法に不安がある

読む章:

1. 第10章 確率の基礎
2. 第11章 数論・代数の基礎
3. 第12章 線形代数の最小限
4. 第13章 並行性と形式モデルの入口

補助:

- 図表: 条件付き確率、Hamming距離、状態インターリーブ
- Python: 確率実験、合同算術、Hamming距離、状態遷移系
- 演習: Extended 演習
- プロジェクト: P5 Hamming距離、P6 RSAデモ、P7 確率実験、P8 状態遷移系

## ミニプロジェクトの使い方

全プロジェクトを実装する必要はない。本体教科書へ進む前の到達確認として、次の組み合わせを推奨する。

| 目的 | 推奨プロジェクト |
|---|---|
| 第1〜3章を固める | P1 関係チェッカー |
| 第6〜8章を固める | P2 BFS、P3 Union-Find |
| 第9章を固める | P4 DFAシミュレータ |
| 第10〜12章を固める | P5 Hamming距離、P7 確率実験 |
| 第11章を固める | P6 合同算術とRSAデモ |
| 第13章を固める | P8 状態遷移系と safety 検査 |

## 完了条件

本体教科書へ進む最低条件:

- 前提診断 80問のうち 60問以上正答。
- Core 演習で 80%以上正答。
- 統合到達確認テストで 70%以上正答。
- 本体教科書 readiness checklist で、読む予定の章の必須項目を満たす。
- 少なくとも1つのミニプロジェクトで、定義・実装・テスト・説明を揃える。

## 参照導線

v1.0 では、次のページから目的別に戻れる。

| 目的 | ページ |
|---|---|
| 章の前後関係を確認する | [章間リンクマップ](navigation/chapter-link-map.md) |
| 本体教科書の章から前提を逆引きする | [本体教科書からの逆引き](navigation/main-textbook-reverse-index.md) |
| 用語を調べる | [用語索引](reference/glossary.md) |
| 記号を調べる | [記号索引](reference/symbol-index.md) |
| 学習進捗を消し込む | [学習チェックリスト](assessment/learning-checklists.md) |
| 研修として運用する | [教員・研修担当者向け運用ガイド](operations/instructor-guide.md) |
| コホートを管理する | [コホート運用ガイド](operations/cohort-operations-guide.md) |
| 提出物を標準化する | [課題提出フォーマット](operations/assignment-submission-format.md) |
| リリースを作る | [リリース手順](operations/release-process.md) |
| 正式公開の監査を確認する | [v1.0 リリース候補監査レポート](audit/v1-release-candidate-audit.md) |
| ライセンス方針を確認する | [ライセンス正式化メモ](audit/license-finalization.md) |
| v1.0公開可否を判定する | [v1.0 リリースチェックリスト](audit/release-checklist-v1.md) |


## v1.0 品質ゲートと運用ゲート

教材更新時は、次を通過してから配布します。

```bash
python scripts/check_links.py
python scripts/check_exercise_labels.py
python scripts/check_exercise_solution_mapping.py
python examples/python/tests.py
python -m pytest
```

受講者運用では、各章の本文後に [章別レビュー問題](review/chapter-review-problems.md) を解き、[採点フォーム](assessment/grading-forms.md) で記録してください。

複数受講者を扱う場合は、[受講者別進捗CSV](forms/learner-progress.csv) と [コホートダッシュボードCSV](forms/cohort-dashboard.csv) をコピーして使います。
