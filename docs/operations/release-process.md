# リリース手順

## 目的

このページは、本教材を継続更新する際のリリース手順を定めます。

v1.0時点では、初回安定版として内容の正確性、ライセンス、引用、品質チェック、配布物の生成手順を固定します。

## バージョン方針

| 種別 | 例 | 意味 |
|---|---|---|
| v0.x | v0.9 | ドラフト。構成変更を許容 |
| v1.0-rc | v1.0-rc | 正式公開前の候補。大きな構成変更を原則禁止 |
| v1.0 | v1.0 | 初回安定版。既存リンクを壊さない |
| v1.1 | v1.1 | 互換性を保つ内容追加 |
| v1.1.1 | v1.1.1 | 誤字、リンク、軽微な修正 |

v1.0以降は、章番号やファイル名の変更を避け、既存リンクを壊さないことを優先します。

## ブランチ運用

```text
main        安定版
develop     次版作業用
feature/*   機能追加
fix/*       誤字・リンク・答案修正
release/*   リリース準備
```

小規模運用では `main` と `feature/*` だけでも構いません。

## リリース前チェック

リリース前に以下を実行します。

```bash
python scripts/check_links.py
python scripts/check_exercise_labels.py
python scripts/check_exercise_solution_mapping.py
python examples/python/tests.py
python -m pytest
bundle exec jekyll build --source docs --config docs/_config.yml --destination _site
```

`bundle exec jekyll build --source docs --config docs/_config.yml --destination _site` はローカルまたはCI環境で実行します。

## 手動確認項目

| 項目 | 確認内容 |
|---|---|
| README | バージョン、スコープ、利用方法が更新されているか |
| CHANGELOG | Added / Changed / Fixed が記録されているか |
| docs/_data/navigation.yml | 新規ページが公開サイトの navigation に含まれているか |
| リンク | 相対リンクが壊れていないか |
| 演習 | 問題番号、難易度ラベル、解答が対応しているか |
| Python examples | tests が通るか |
| ライセンス | 公開形態と矛盾していないか |
| 引用 | 外部教材の本文・図・問題を転載していないか |

チェックリストは [リリースチェックリスト](../forms/release-checklist.md) を使います。

## 配布物の作成

ZIPを作成する例です。

```bash
VERSION=v1.0
DIR=theoretical-computer-science-prerequisites-book-${VERSION}
zip -r ${DIR}.zip ${DIR} \
  -x "*/.git/*" \
  -x "*/.pytest_cache/*" \
  -x "*/site/*" \
  -x "*/__pycache__/*"
```

このリポジトリには、簡易パッケージング用の `scripts/package_release.py` も含めています。

```bash
python scripts/package_release.py --version v1.0 --suffix release
```

## リリースノート雛形

```text
## vX.Y

### Added

- 

### Changed

- 

### Fixed

- 

### Validation

- python scripts/check_links.py
- python scripts/check_exercise_labels.py
- python examples/python/tests.py
- python -m pytest
- bundle exec jekyll build --source docs --config docs/_config.yml --destination _site

### Known limitations

- 
```

## ロールバック

リリース後に重大な誤りが見つかった場合は、次の順で対応します。

1. 該当ページの公開を止める、または冒頭に注意書きを入れる。
2. issueを作成する。
3. 修正ブランチで最小修正を行う。
4. パッチ版を作成する。
5. CHANGELOGに誤りと修正内容を記録する。

## リリース判定

次のいずれかが残っている場合は、リリースしません。

- リンクチェックが失敗している。
- 演習と解答の番号が対応していない。
- 証明問題の解答が例示だけで終わっている。
- 外部教材の文章・図・問題の流用可能性がある。
- ライセンス方針が未定のまま外部公開しようとしている。
