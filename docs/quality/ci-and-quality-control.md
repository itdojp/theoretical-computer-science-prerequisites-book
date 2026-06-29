# CIと品質管理

## 目的

教材を継続更新する前提で、最低限の品質ゲートを定義する。v1.0 では、リンク、演習ラベル、演習と解答の番号対応、Python examples、MkDocs build を確認対象にする。

## ローカル確認

```bash
python scripts/check_links.py
python scripts/check_exercise_labels.py
python scripts/check_exercise_solution_mapping.py
python examples/python/tests.py
python -m pytest
```

MkDocsをインストールできる環境では、次も実行する。

```bash
pip install -r requirements.txt
mkdocs build --strict
```

## GitHub Actions

`.github/workflows/ci.yml` は以下を実行する。

- Python 3.11 のセットアップ。
- `requirements.txt` のインストール。
- Markdownリンクチェック。
- 演習難易度ラベルチェック。
- 演習番号と解答番号の対応チェック。
- pytest。
- 既存の smoke test。
- MkDocs strict build。

## 失敗時の処理

| 失敗箇所 | 典型原因 | 対応 |
|---|---|---|
| `check_links.py` | 相対リンク先の変更、ファイル名変更 | リンクまたはファイル名を修正 |
| `check_exercise_labels.py` | 新規演習に難易度ラベルがない | `[A]〜[E]` のラベルを付与 |
| `check_exercise_solution_mapping.py` | 問題追加後に解答を追加していない、番号ずれ | 問題IDと解答IDを揃える |
| `pytest` | exampleの仕様変更、境界条件未対応 | テストまたは実装を更新 |
| `examples/python/tests.py` | smoke testの退行 | 既存API互換性を確認 |
| `mkdocs build --strict` | nav参照先不備、Markdown拡張の問題 | `mkdocs.yml` と対象Markdownを修正 |

## 品質ゲート

Pull Request またはリリース前に、次の条件を満たすこと。

- 追加・変更したMarkdownの相対リンクが通る。
- Python exampleのテストが通る。
- 新規演習には難易度ラベルが付いている。
- 新規演習には対応する解答または採点観点がある。
- 新規章には「この章で使う記号」「次に読む章」がある。
- 本体教科書への接続が少なくとも1箇所明示されている。
- スコープ境界監査に反する内容を追加していない。

## リリース候補の追加確認

v1.0 系のリリース候補では、次も確認する。

- [v1.0 リリース候補監査レポート](../audit/v1-release-candidate-audit.md)
- [演習番号と解答番号の対応監査](../audit/exercise-solution-mapping.md)
- [ライセンス正式化メモ](../audit/license-finalization.md)
- [v1.0 リリースチェックリスト](../audit/release-checklist-v1.md)
