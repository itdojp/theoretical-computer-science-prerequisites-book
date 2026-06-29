# GitHub 初回投入手順

対象リポジトリ:

```text
https://github.com/itdojp/theoretical-computer-science-prerequisites-book
```

## 1. ローカルで初回コミットして push する

このパッケージを展開したディレクトリで実行する。

```bash
git init
git branch -M main
git add .
git commit -m "Initial release: theoretical computer science prerequisites book"
git remote add origin git@github.com:itdojp/theoretical-computer-science-prerequisites-book.git
git push -u origin main
```

HTTPS を使う場合:

```bash
git remote add origin https://github.com/itdojp/theoretical-computer-science-prerequisites-book.git
git push -u origin main
```

既に remote がある場合:

```bash
git remote set-url origin git@github.com:itdojp/theoretical-computer-science-prerequisites-book.git
git push -u origin main
```

## 2. GitHub Pages を有効化する

GitHub のリポジトリ画面で次を設定する。

```text
Settings
  → Pages
  → Build and deployment
  → Source: GitHub Actions
```

`.github/workflows/pages.yml` が `main` への push 時に Jekyll を build し、GitHub Pages へ deploy する。

## 3. 動作確認

Actions が通過した後、次のURLを確認する。

```text
https://itdojp.github.io/theoretical-computer-science-prerequisites-book/
```

## 4. GitHub Release を作る

```bash
git tag v1.0
git push origin v1.0
```

GitHub Release の本文は次を使う。

```text
docs/release/github-release-notes-v1.0.md
```

## 5. 知識アーキテクチャへ追加する

追加用の文案は次を使う。

```text
integration/knowledge-architecture-addition.md
```
