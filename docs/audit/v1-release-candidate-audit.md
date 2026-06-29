# v1.0 リリース候補監査レポート

## 目的

このページは、v1.0 正式公開前に確認すべき品質・構成・運用・ライセンス観点を一箇所に集約する。

v1.0-rc は、v1.0正式版へ進む前の候補版として、教材を配布可能な状態へ近づけるための監査版である。

## 監査対象

| 項目 | 対象 | 判定 |
|---|---|---|
| 章構成 | Core 5章、Standard 4章、Extended 4章 | 合格 |
| 評価導線 | 前提診断、章末確認、演習、統合テスト、readiness checklist | 合格 |
| 演習 | Core / Standard / Extended / ドリル / 統合テスト | 合格 |
| 解答 | Core / Standard / Extended / 統合テスト | 合格 |
| レビュー問題 | 章別レビュー問題と採点観点 | 合格。ただし完全解答ではなく採点メモ |
| 図表 | 静的SVG図、図表ガイド | 合格 |
| Python実装 | examples、smoke test、pytest | 合格 |
| ナビゲーション | MkDocs nav、章間リンク、逆引き | 合格 |
| 運用文書 | 研修、コホート、輪読、リリース、メンテナンス | 合格 |
| ライセンス | ITDO Inc. 統一ライセンス 文書追加 | v1.0では正式方針として採用 |
| MkDocs build | `mkdocs build --strict` | 公開環境またはCI環境で確認する |

## v1.0-rc で追加した品質ゲート

- 演習と解答の番号対応を確認する `scripts/check_exercise_solution_mapping.py`。
- ライセンス正式化メモ。
- 表記・用語スタイルガイド。
- スコープ境界監査。
- v1.0 リリースチェックリスト。

## 自動検査対象

```bash
python scripts/check_links.py
python scripts/check_exercise_labels.py
python scripts/check_exercise_solution_mapping.py
python examples/python/tests.py
python -m pytest
```

## 自動検査対象外

次は人手確認が必要である。

- 数学的証明の厳密性。
- 章別レビュー問題の採点観点の妥当性。
- 外部教材名・リンク・ライセンスの最新性。
- 商用研修利用時のライセンス適合性。
- MkDocs Material の実ブラウザ表示。

## v1.0 へ進める条件

- 上記の自動検査がすべて通過する。
- `mkdocs build --strict` が公開環境またはCI環境で通過する。
- `LICENSE`、`LICENSE-DOCS.md`、`LICENSE-CODE.md` の方針を公開主体として承認する。
- README の著作者・問い合わせ先・公開URLを実運用に合わせて必要に応じて更新する。
- 本体教科書側からのリンク方針を決める。
