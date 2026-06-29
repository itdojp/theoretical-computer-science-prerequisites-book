# v1.0 公開手順

## 1. 公開前確認

```bash
python scripts/check_links.py
python scripts/check_exercise_labels.py
python scripts/check_exercise_solution_mapping.py
python examples/python/tests.py
python -m pytest
bundle exec jekyll build --source docs --config docs/_config.yml --destination _site
```

`bundle exec jekyll build --source docs --config docs/_config.yml --destination _site` は `bundle install` 後に実行します。

## 2. 公開メタデータを確定する

次を確認します。

- GitHubリポジトリURL。
- GitHub Pages URL または公開先URL。
- 問い合わせ先をIssueに限定するか、別連絡先を置くか。
- 著作者表記を contributors のままにするか、組織名義にするか。
- `CITATION.cff` の著作者表記。
- `docs/_config.yml` の `url` / `baseurl` が公開URLと一致しているか。

## 3. タグを作成する

```bash
git tag -a v1.0 -m "Release v1.0"
git push origin v1.0
```

## 4. 配布ZIPを作成する

```bash
python scripts/package_release.py --version v1.0 --suffix release --output-dir dist
```

必要なら、ファイル名を公開ポリシーに合わせて変更します。

## 5. GitHub Release本文を作る

`docs/release/github-release-notes-v1.0.md` の内容をGitHub Release本文に使います。

## 6. 公開後確認

- GitHub ReleaseのZIPが展開できる。
- GitHub Pagesのトップページが開ける。
- 主要ページの検索・数式・コードブロックが表示される。
- READMEのリンクが公開先で壊れていない。
- Issue / PRテンプレートが表示される。

## 7. 公開後の変更方針

- 誤字、リンク修正、軽微な解答修正は `v1.0.x`。
- ページ追加、演習追加、運用文書追加は `v1.1`。
- 章番号、既存ファイル名、演習IDの破壊的変更は避ける。
