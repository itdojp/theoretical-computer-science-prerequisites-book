# 理論計算機科学を読むための数学・証明・アルゴリズム基礎

## この教材の位置づけ

この教材は、理論計算機科学の本編を読むための前提を補う「前処理」です。理論計算機科学そのものの全範囲を説明する教材ではありません。

本教材のゴールは次の状態を作ることです。

1. 集合・論理・関数・関係の定義を読める。
2. 定義から証明を書き始められる。
3. 数学的帰納法と構造帰納法を使える。
4. O記法を定義と直観の両方で理解している。
5. 擬似コードと短いプログラムの挙動を追える。
6. グラフ、木、到達可能性、探索を最低限扱える。
7. 組合せ・鳩ノ巣原理・包除原理を使って候補数を見積もれる。
8. 主要なデータ構造の操作と計算量を説明できる。
9. 文字列・言語・文法・DFA/NFA の基本記法を読める。
10. 条件付き確率、期待値、確率変数、指示変数を扱える。
11. 剰余計算、逆元、群、体の基本記法を読める。
12. 行列、ランク、`F_2` 上の線形代数、線形符号の入口を読める。
13. 状態遷移、非決定性、safety/liveness、合意問題の入口を読める。
14. 図表を使って直観を確認し、定義へ戻れる。
15. Python実装で小さい例を検査できる。
16. ミニプロジェクトで定義・証明・実装を接続できる。
17. 本体教科書のどの章で、どの前提が使われるかを把握している。
18. 自分の弱点を診断し、該当章・該当演習へ戻れる。
19. 本体教科書の各章へ進む前に、readiness checklist で進行可否を判断できる。
20. 用語索引・記号索引・章間リンクから必要箇所へ戻れる。
21. 教員・研修担当者が診断、提出、レビュー、再提出、本体教科書への進行判定を運用できる。
22. メンテナがCI、リリース、ライセンス、コントリビューションを管理できる。

## 学習順序

標準ルート:

```text
前提診断
  ↓
採点ルーブリックで採点
  ↓
弱点別リカバリールートを確認
  ↓
第1章〜第13章の必要箇所を学習
  ↓
図表で直観を確認
  ↓
Python実装ノートと examples で小さい例を動かす
  ↓
Core / Standard / Extended 演習
  ↓
統合到達確認テスト
  ↓
ミニプロジェクトを1〜2個実装
  ↓
本体教科書 readiness checklist
  ↓
本体教科書へ
```

## v1.0 で重視した追加要素

v1.0 では、初回安定版として、学習導線、演習運用、品質管理、公開手順、ライセンス文書を整備しています。

- v1.0 リリース監査レポート
- 表記・用語スタイルガイド
- 演習番号と解答番号の対応監査
- スコープ境界監査
- ライセンス正式化メモ
- v1.0 リリースチェックリスト
- 演習解答対応チェック用スクリプト
- ITDO Inc. 統一ライセンス 文書
- Citation metadata
- GitHub Release用ノート
- 公開メタデータ雛形

## 目次

### 導入

- [前提診断](diagnosis.md)
- [学習ルート](learning-path.md)

### Part I Core

- [第1章 集合と論理](part-1-core/01-sets-logic.md)
- [第2章 関数と関係](part-1-core/02-functions-relations.md)
- [第3章 証明技法](part-1-core/03-proofs.md)
- [第4章 漸近記法](part-1-core/04-asymptotic-notation.md)
- [第5章 擬似コードと再帰](part-1-core/05-pseudocode-recursion.md)

### Part II Standard

- [第6章 グラフと木](part-2-standard/06-graphs-trees.md)
- [第7章 組合せと数え上げ](part-2-standard/07-counting.md)
- [第8章 データ構造と基本アルゴリズム](part-2-standard/08-data-structures.md)
- [第9章 形式言語の入口](part-2-standard/09-formal-language-primer.md)

### Part III Extended

- [第10章 確率の基礎](part-3-extended/10-probability.md)
- [第11章 数論・代数の基礎](part-3-extended/11-number-theory-algebra.md)
- [第12章 線形代数の最小限](part-3-extended/12-linear-algebra.md)
- [第13章 並行性と形式モデルの入口](part-3-extended/13-concurrency-models.md)

### ナビゲーション

- [ナビゲーションガイド](navigation/navigation-guide.md)
- [章間リンクマップ](navigation/chapter-link-map.md)
- [本体教科書からの逆引き](navigation/main-textbook-reverse-index.md)

### 用語・索引

- [用語索引](reference/glossary.md)
- [記号索引](reference/symbol-index.md)
- [概念別逆引き](reference/concept-index.md)

### 図表

- [図表ガイド](visual/visual-index.md)
- [証明・漸近記法・再帰](visual/proof-and-logic-diagrams.md)
- [グラフ・データ構造・オートマトン](visual/graph-and-automata-diagrams.md)
- [確率・符号・並行性](visual/probability-linear-concurrency-diagrams.md)

### Python実装ノート

- [実装方針](python/python-implementation-notes.md)
- [アルゴリズムとデータ構造](python/algorithm-snippets.md)
- [形式言語とオートマトン](python/automata-coding.md)
- [確率・数論・線形代数・状態遷移](python/probability-linear-algebra-coding.md)

### 例題・プロジェクト

- [章別例題集](examples/worked-examples-by-chapter.md)
- [ミニプロジェクト](projects/mini-projects.md)
- [ミニプロジェクト採点基準](projects/project-rubrics.md)

### 評価・到達判定

- [採点ルーブリック](assessment/scoring-rubric.md)
- [到達判定表](assessment/attainment-criteria.md)
- [章末確認チェック](assessment/chapter-exit-checks.md)
- [弱点別リカバリールート](assessment/recovery-routes.md)
- [本体教科書 readiness checklist](assessment/main-textbook-readiness.md)
- [学習チェックリスト](assessment/learning-checklists.md)

### 演習

- [Core 演習](exercises/core-exercises.md)
- [Core 演習 完全解答](exercises/solutions.md)
- [Standard 演習](exercises/standard-exercises.md)
- [Standard 演習 解答](exercises/standard-solutions.md)
- [Extended 演習](exercises/extended-exercises.md)
- [Extended 演習 解答](exercises/extended-solutions.md)
- [証明ドリル](exercises/proof-drills.md)
- [漸近記法ドリル](exercises/asymptotic-drills.md)
- [擬似コード・再帰ドリル](exercises/pseudocode-recursion-drills.md)
- [演習難易度インデックス](exercises/difficulty-index.md)
- [統合到達確認テスト](exercises/integrated-readiness-test.md)
- [統合到達確認テスト 解答](exercises/integrated-readiness-solutions.md)


### 運用

- [教員・研修担当者向け運用ガイド](operations/instructor-guide.md)
- [コホート運用ガイド](operations/cohort-operations-guide.md)
- [レビュー会・輪読会の進行手順](operations/reading-group-facilitation.md)
- [課題提出フォーマット](operations/assignment-submission-format.md)
- [受講者別進捗管理テンプレート](operations/learner-progress-template.md)
- [リリース手順](operations/release-process.md)
- [コントリビューションガイド](operations/contribution-guide.md)
- [ライセンス・引用ポリシー](operations/license-and-citation-policy.md)
- [メンテナンス・プレイブック](operations/maintenance-playbook.md)

### 監査・正式公開準備

- [v1.0 リリース候補監査レポート](audit/v1-release-candidate-audit.md)
- [表記・用語スタイルガイド](audit/style-and-terminology.md)
- [演習番号と解答番号の対応監査](audit/exercise-solution-mapping.md)
- [スコープ境界監査](audit/scope-boundary-audit.md)
- [ライセンス正式化メモ](audit/license-finalization.md)
- [v1.0 リリースチェックリスト](audit/release-checklist-v1.md)

### テンプレート

- [課題提出テンプレート](forms/assignment-submission.md)
- [レビュー会議事録テンプレート](forms/review-meeting-notes.md)
- [リリースチェックリスト](forms/release-checklist.md)
- [Issueテンプレート](forms/issue-template.md)
- [Pull Requestテンプレート](forms/pull-request-template.md)
- [受講者別進捗CSV](forms/learner-progress.csv)
- [コホートダッシュボードCSV](forms/cohort-dashboard.csv)

### 付録

- [記号一覧](appendix/notation.md)
- [証明テンプレート集](appendix/proof-templates.md)
- [本体教科書との対応表](appendix/mapping-to-main-textbook.md)


## v1.0 の追加導線

- 監査全体: [v1.0 リリース候補監査レポート](audit/v1-release-candidate-audit.md)
- 表記統一: [表記・用語スタイルガイド](audit/style-and-terminology.md)
- 解答対応: [演習番号と解答番号の対応監査](audit/exercise-solution-mapping.md)
- スコープ確認: [スコープ境界監査](audit/scope-boundary-audit.md)
- ライセンス確認: [ライセンス正式化メモ](audit/license-finalization.md)
- リリース判定: [v1.0 リリースチェックリスト](audit/release-checklist-v1.md)
- 更新時の品質確認: [CIと品質管理](quality/ci-and-quality-control.md)

### リリース

- [公開メタデータ](release/release-metadata.md)
- [GitHub Release Notes](release/github-release-notes-v1.0.md)
- [公開手順](release/publication-guide.md)
- [v1.0 最終監査メモ](release/final-release-audit.md)

