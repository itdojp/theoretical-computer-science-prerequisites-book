# 受講者別進捗管理テンプレート

## 目的

このページは、受講者ごとの診断結果、演習進捗、レビュー状況、本体教科書への進行可否を管理するためのテンプレート仕様です。

CSVテンプレートは次です。

- [受講者別進捗CSV](../forms/learner-progress.csv)
- [コホートダッシュボードCSV](../forms/cohort-dashboard.csv)

## 受講者別進捗CSVの列

| 列 | 意味 |
|---|---|
| learner_id | 受講者を識別するID。実名でなくてよい |
| cohort_id | コホートID |
| diagnostic_score | 前提診断の点数 |
| core_status | Coreの状態 |
| standard_status | Standardの状態 |
| extended_status | Extendedの状態 |
| review_score_avg | 章別レビュー問題の平均点 |
| integrated_test_score | 統合到達確認テストの点数 |
| mini_project_score | ミニプロジェクトの点数 |
| readiness_status | 本体教科書へ進めるか |
| next_action | 次にやるべきこと |
| reviewer | レビュー担当 |
| last_updated | 最終更新日 |

## ステータス値

| 値 | 意味 |
|---|---|
| not_started | 未着手 |
| in_progress | 学習中 |
| needs_remediation | 補強が必要 |
| passed | 合格 |
| skipped | 診断結果により省略 |
| deferred | 一時停止 |

## 更新タイミング

| タイミング | 更新する列 |
|---|---|
| 前提診断後 | diagnostic_score, next_action |
| 章別レビュー後 | review_score_avg, core_status など |
| 統合テスト後 | integrated_test_score, readiness_status |
| ミニプロジェクト後 | mini_project_score, readiness_status |
| 再提出後 | next_action, last_updated |

## 読み方

`readiness_status` が `ready` でも、全章を理解したことを意味しません。対象の本体章へ入る最低前提を満たしたという意味です。

## 推奨運用

- 個人情報を入れない。
- 受講者本人とレビュー担当が確認できる場所に置く。
- 毎週1回だけ更新し、細かすぎる管理を避ける。
- 点数だけでなく、`next_action` に具体的な補強対象を書く。

例:

```text
next_action = 第3章の構造帰納法を再提出。第4章には進まない。
```
