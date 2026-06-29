# リリースチェックリスト

## 基本情報

- version:
- release branch:
- release owner:
- date:

## 内容確認

- [ ] READMEのバージョンとスコープを更新した。
- [ ] CHANGELOGにAdded / Changed / Fixedを記載した。
- [ ] 新規ページをmkdocs.ymlへ追加した。
- [ ] index.mdに主要導線を追加した。
- [ ] learning-path.mdに必要な導線を追加した。
- [ ] 新規演習には難易度ラベルを付けた。
- [ ] 新規演習には解答または採点観点を付けた。
- [ ] 用語・記号の表記を既存索引と揃えた。

## 品質チェック

```bash
python scripts/check_links.py
python scripts/check_exercise_labels.py
python examples/python/tests.py
python -m pytest
mkdocs build --strict
```

- [ ] リンクチェック通過。
- [ ] 演習ラベルチェック通過。
- [ ] Python examples smoke test 通過。
- [ ] pytest 通過。
- [ ] mkdocs build --strict 通過。

## ライセンス・引用

- [ ] 外部教材の本文・図・問題を転載していない。
- [ ] 引用・参照が必要な箇所を確認した。
- [ ] ライセンス方針と配布形態が矛盾していない。
- [ ] 商用利用する場合の条件を確認した。

## 配布物

- [ ] ZIPを作成した。
- [ ] ZIPを展開してファイル構成を確認した。
- [ ] 不要なキャッシュやsiteディレクトリが含まれていない。
- [ ] Gitタグを作成した。
- [ ] リリースノートを作成した。

## 既知の制限

-
