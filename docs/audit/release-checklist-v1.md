# v1.0 リリースチェックリスト

## 1. 自動検査

- [ ] `python scripts/check_links.py` が通過する。
- [ ] `python scripts/check_exercise_labels.py` が通過する。
- [ ] `python scripts/check_exercise_solution_mapping.py` が通過する。
- [ ] `python examples/python/tests.py` が通過する。
- [ ] `python -m pytest` が通過する。
- [ ] 実環境で `mkdocs build --strict` が通過する。

## 2. 内容監査

- [ ] 第1章〜第13章の章タイトルと本文が一致している。
- [ ] 章冒頭の記号一覧と `docs/reference/symbol-index.md` が矛盾しない。
- [ ] 用語索引に主要語が登録されている。
- [ ] 演習の難易度ラベルが付いている。
- [ ] 解答が問題番号と対応している。
- [ ] 統合到達確認テストの合格条件が README と評価ページで矛盾しない。
- [ ] 章別レビュー問題が「完全解答」ではなく「採点観点」であることを明示している。

## 3. ライセンス・引用

- [ ] `LICENSE` が存在する。
- [ ] `LICENSE-DOCS.md` が存在する。
- [ ] `LICENSE-CODE.md` が存在する。
- [ ] `LICENSE-POLICY.md` が現方針と矛盾しない。
- [ ] `docs/audit/license-finalization.md` が更新済みである。
- [ ] 外部教材の本文・図・問題を転載していない。
- [ ] 外部リンクは参照として扱い、各外部教材のライセンスを尊重している。

## 4. 運用

- [ ] `docs/operations/instructor-guide.md` が最新構成に対応している。
- [ ] `docs/operations/release-process.md` の VERSION 例が更新されている。
- [ ] `docs/forms/release-checklist.md` が v1.0 と矛盾しない。
- [ ] GitHub Issue / PR テンプレートが存在する。
- [ ] `CITATION.cff` が存在する。

## 5. 公開前メタデータ

- [ ] README の著作者名が確定している。
- [ ] README の公開URLが確定している。
- [ ] `site_author` が確定している。
- [ ] `site_url` を使う場合は `mkdocs.yml` に追加している。
- [ ] 連絡先またはIssue受付方針が明記されている。

## 6. リリース作業

- [ ] `CHANGELOG.md` の v1.0 セクションを確定する。
- [ ] タグ名を決める。例: `v1.0.0`。
- [ ] `python scripts/package_release.py --version v1.0.0 --suffix release` を実行する。
- [ ] ZIPを展開して `unzip -t` を実行する。
- [ ] GitHub Release本文に変更点、互換性、既知の未確認事項を書く。

## 7. v1.0 リリース不可条件

次のいずれかが残る場合は v1.0 として公開しない。

- 自動検査の失敗。
- 演習と解答の番号ずれ。
- ライセンス方針未承認。
- 外部教材の無断転載疑義。
- MkDocs build の重大エラー。
