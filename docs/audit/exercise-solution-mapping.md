# 演習番号と解答番号の対応監査

## 目的

演習問題と解答の番号ずれを防ぐ。v1.0 では、主要演習セットについて自動検査を追加する。

## 対象

| 演習 | 問題ファイル | 解答ファイル | 監査方法 |
|---|---|---|---|
| Core 演習 | `docs/exercises/core-exercises.md` | `docs/exercises/solutions.md` | 1〜70 の番号一致 |
| Standard 演習（第7〜9章） | `docs/exercises/standard-exercises.md` | `docs/exercises/standard-solutions.md` | S1〜S60 の番号一致 |
| Standard グラフ演習（第6章） | `docs/exercises/standard-exercises.md` | `docs/exercises/standard-solutions.md` | G1〜G12 の番号一致 |
| Extended 演習 | `docs/exercises/extended-exercises.md` | `docs/exercises/extended-solutions.md` | E1〜E80 の番号一致 |
| 統合到達確認テスト | `docs/exercises/integrated-readiness-test.md` | `docs/exercises/integrated-readiness-solutions.md` | Q1〜Q50 と A1〜A50 の番号一致 |

## 対象外

章別レビュー問題は、現時点では完全解答ではなく「採点観点」として運用する。そのため、問題番号と解答番号の完全一致チェックの対象外とする。v1.0 正式公開後に完全解答化する場合は、各章5問に対して `R1-1` 形式などの安定IDを付与する。

## 実行方法

```bash
python scripts/check_exercise_solution_mapping.py
```

## 合格条件

- 問題側にあるIDがすべて解答側にも存在する。
- 解答側に、問題側に存在しないIDがない。
- Core は 70問、Standard は 60問、Extended は 80問、統合到達確認テストは 50問である。

## 監査結果

v1.0 生成時点では、上記スクリプトで対応確認を行う。
