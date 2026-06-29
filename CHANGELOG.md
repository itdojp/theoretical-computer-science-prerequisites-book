# Changelog

## v1.0

### Added

- 初回安定版として `VERSION` と `RELEASE.md` を追加。
- v1.0 公開メタデータを追加。
- GitHub Release用ノートを追加。
- v1.0 公開手順を追加。
- v1.0 最終監査メモを追加。

### Changed

- README、NOTICE、LICENSE-POLICY、CITATION、mkdocs.yml を v1.0 に更新。
- リリース手順を v1.0 安定版前提に更新。
- ライセンス正式化メモを v1.0 の正式方針へ更新。

### Validation

- `python scripts/check_links.py`
- `python scripts/check_exercise_labels.py`
- `python scripts/check_exercise_solution_mapping.py`
- `python examples/python/tests.py`
- `python -m pytest`
- ZIP整合性確認

## v1.0-rc

### Added

- v1.0 リリース候補監査レポートを追加。
- 表記・用語スタイルガイドを追加。
- 演習番号と解答番号の対応監査を追加。
- スコープ境界監査を追加。
- ライセンス正式化メモを追加。
- v1.0 リリースチェックリストを追加。
- `LICENSE`、`LICENSE-DOCS.md`、`LICENSE-CODE.md` を追加。
- `CITATION.cff` を追加。
- 演習と解答の番号対応を確認する `scripts/check_exercise_solution_mapping.py` を追加。

### Changed

- README を v1.0-rc に更新。
- index と learning-path に監査・正式公開準備への導線を追加。
- mkdocs.yml のナビゲーションに監査・正式公開準備セクションを追加。
- CIと品質管理ガイドに演習解答対応チェックを追加。
- GitHub Actions に演習解答対応チェックを追加。
- ライセンス・引用ポリシーを ITDO Inc. 統一ライセンス 前提に更新。
- リリース手順の例を v1.0-rc に更新。
- tests/test_project_layout.py に v1.0-rc の必須ファイルを追加。

## v0.9 draft

### Added

- 教員・研修担当者向け運用ガイドを追加。
- コホート運用ガイドを追加。
- レビュー会・輪読会の進行手順を追加。
- 課題提出フォーマットを追加。
- 受講者別進捗管理テンプレートを追加。
- リリース手順を追加。
- コントリビューションガイドを追加。
- ライセンス・引用ポリシーを追加。
- メンテナンス・プレイブックを追加。
- 課題提出、レビュー会議事録、リリースチェックリストのMarkdownテンプレートを追加。
- 受講者別進捗、コホートダッシュボードのCSVテンプレートを追加。
- GitHub Issue / Pull Request テンプレートを追加。
- 簡易パッケージングスクリプトを追加。
- `CONTRIBUTING.md` と `LICENSE-POLICY.md` を追加。

### Changed

- README を v0.9 に更新。
- index に運用・テンプレート導線を追加。
- learning-path に研修運用・進捗管理・リリース管理への導線を追加。
- mkdocs.yml のナビゲーションに運用・テンプレートを追加。
- tests/test_project_layout.py に v0.9 の必須ファイルを追加。

## v0.8 draft

### Added

- 章別レビュー問題を追加。
- 章別レビュー問題の解答・採点観点を追加。
- 採点フォームとCSVテンプレートを追加。
- 難易度ラベル付き演習インデックスを追加。
- CIと品質管理ガイドを追加。
- Markdownリンクチェック用スクリプトを追加。
- 演習ラベルチェック用スクリプトを追加。
- pytest 化された Python examples テストを追加。
- GitHub Actions 設定を追加。

### Changed

- Core / Standard / Extended / ドリル / 統合到達確認テストの演習問題に難易度ラベルを直接付与。
- requirements に pytest を追加。
- mkdocs.yml のナビゲーションにレビュー問題、採点フォーム、品質管理を追加。
- README を v0.8 に更新。

## v0.7 draft

### Added

- MkDocs Material 対応設定を追加。
- `requirements.txt` を追加。
- ナビゲーションガイドを追加。
- 章間リンクマップを追加。
- 本体教科書からの逆引きを追加。
- 用語索引、記号索引、概念別逆引きを追加。
- 学習チェックリストを追加。
- 各章冒頭に「この章で使う記号」を追加。
- 各章冒頭に章間ナビゲーションを追加。
- 各章末に「次に読む章」を追加。

### Changed

- README を v0.7 に更新。
- index にナビゲーションと用語・索引セクションを追加。
- learning-path に参照導線を追加。
- mkdocs.yml を Material 前提の設定に更新。

## v0.6 draft

### Added

- 図表ガイドを追加。
- 静的SVG図を追加。
  - 証明フロー
  - 成長率比較
  - 再帰スタック
  - BFS距離層
  - Union-Find
  - DFA / NFA
  - 条件付き確率の確率木
  - Hamming距離
  - 並行実行のインターリーブ
  - ループ不変条件
- Python実装ノートを追加。
- 実行可能な Python examples を追加。
  - 再帰トレース
  - BFS
  - Union-Find
  - DFAシミュレータ
  - Hamming距離
  - 合同算術
  - 確率実験
  - 状態遷移系
- 章別例題集を追加。
- ミニプロジェクト仕様を追加。
- ミニプロジェクト採点基準を追加。

### Changed

- README を v0.6 に更新。
- index に図表、Python実装、例題・プロジェクトの導線を追加。
- learning-path に実装補強フェーズを追加。
- mkdocs.yml のナビゲーションを v0.6 対応に更新。

## v0.5 draft

### Added

- 採点ルーブリックを追加。
- Core / Standard / Extended の到達判定表を追加。
- 章末確認チェックを追加。
- 弱点別リカバリールートを追加。
- 本体教科書 readiness checklist を追加。
- 演習難易度インデックスを追加。
- 統合到達確認テスト 50問を追加。
- 統合到達確認テストの解答を追加。

### Changed

- README を v0.5 に更新。
- index に評価・到達判定セクションを追加。
- learning-path に領域別得点・合格条件・ワークフローを追加。
- mkdocs.yml のナビゲーションに評価・到達判定と統合テストを追加。

## v0.4 draft

### Added

- Extended 領域を追加。
- 第10章 確率の基礎を追加。
- 第11章 数論・代数の基礎を追加。
- 第12章 線形代数の最小限を追加。
- 第13章 並行性と形式モデルの入口を追加。
- Extended 演習 80問を追加。
- Extended 解答 80問を追加。
- 前提診断を80問へ拡張。

## v0.3 draft

### Added

- Standard 領域を追加。
- 第7章 組合せと数え上げを追加。
- 第8章 データ構造と基本アルゴリズムを追加。
- 第9章 形式言語の入口を追加。
- Standard 演習 60問を追加。
- Standard 解答 60問を追加。

## v0.2 draft

### Added

- 第3章 証明技法を拡充。
- 第4章 漸近記法を拡充。
- 第5章 擬似コードと再帰を拡充。
- 証明ドリル、漸近記法ドリル、擬似コード・再帰ドリルを追加。
- Core 演習の解答を完全化。

## v0.1 draft

### Added

- 初版ドラフト。
- Core 5章、グラフ章、Core 演習、対応表を追加。
