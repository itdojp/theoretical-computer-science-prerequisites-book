# GitHub Release Notes: v1.0

## 概要

`v1.0` は、『理論計算機科学教科書』を読む前に不足しやすい前提知識を補うための初回安定版です。

集合・論理・証明・漸近記法・擬似コード・グラフ・組合せ・データ構造・形式言語・確率・数論・線形代数・並行性モデルを、診断、本文、演習、解答、図表、Python実装、ミニプロジェクト、到達判定の形で整理しています。

## 主な内容

- 前提診断 80問。
- 第1章〜第13章の本文。
- Core / Standard / Extended 演習と解答。
- 証明・漸近記法・擬似コード・再帰の追加ドリル。
- 統合到達確認テスト 50問と解答。
- 章別レビュー問題と採点観点。
- 採点ルーブリック、到達判定表、弱点別リカバリールート。
- 本体教科書 readiness checklist。
- 図表、Python実装ノート、実行可能な Python examples。
- ミニプロジェクトと採点基準。
- MkDocs Material 用設定。
- 用語索引、記号索引、概念別逆引き。
- 研修運用ガイド、コホート運用ガイド、提出テンプレート。
- CI用チェックスクリプト、pytest、GitHub Actions設定。
- ライセンス文書、Citation metadata、公開メタデータ。

## 検証

リリースパッケージ作成時点で次を確認しています。

```bash
python scripts/check_links.py
python scripts/check_exercise_labels.py
python scripts/check_exercise_solution_mapping.py
python examples/python/tests.py
python -m pytest
```

`mkdocs build --strict` は、MkDocs / MkDocs Material をインストールした公開環境またはCI環境で確認してください。

## 互換性

v1.0以降は、既存リンクを壊さないことを優先します。章番号、ファイル名、演習IDの変更は原則として避けます。

## ライセンス

- 本文・図表・演習・解答・テンプレート: CC BY-NC-SA 4.0
- Python examples、scripts、tests、CI設定: CC BY-NC-SA 4.0

詳細は `LICENSE`、`LICENSE-DOCS.md`、`LICENSE-CODE.md` を参照してください。

## 既知の運用上の注意

- 公開URL、問い合わせ先、組織名義の著作者表記は `itdojp/theoretical-computer-science-prerequisites-book` 向けに設定済みです。
- GitHub Pages を利用する場合は、Repository Settings → Pages → Build and deployment → Source を GitHub Actions に設定してください。
- 商用研修で利用する場合は、ITDO Inc. の商用ライセンス契約が必要です。
