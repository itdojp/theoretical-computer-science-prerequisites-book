# ITエンジニア知識アーキテクチャ追加用メモ

対象リポジトリ:

```text
https://github.com/itdojp/it-engineer-knowledge-architecture
```

追加する書籍:

```text
書籍名: 理論計算機科学を読むための数学・証明・アルゴリズム基礎
Repository: https://github.com/itdojp/theoretical-computer-science-prerequisites-book
Pages: https://itdojp.github.io/theoretical-computer-science-prerequisites-book/
カテゴリ: コンピューターサイエンス理論
配置: 「理論計算機科学教科書」の直前
```

## `docs/index.md` の更新

### 概要カウント

現在の値に +1 する。

```diff
-- 既存書籍: 39冊（レビュー済み）
-- 合計: 46冊による総合的な知識体系
+- 既存書籍: 40冊（レビュー済み）
+- 合計: 47冊による総合的な知識体系
```

「レビュー完了後の読み方」にある `既存書籍 39 冊` も `既存書籍 40 冊` に更新する。

### 書籍一覧: コンピューターサイエンス理論

`#### コンピューターサイエンス理論` の直後で、既存の `理論計算機科学教科書` の前に挿入する。

```markdown
22. 理論計算機科学を読むための数学・証明・アルゴリズム基礎
[書籍を読む](https://itdojp.github.io/theoretical-computer-science-prerequisites-book/) | [リポジトリ](https://github.com/itdojp/theoretical-computer-science-prerequisites-book)

23. 理論計算機科学教科書
[書籍を読む](https://itdojp.github.io/theoretical-computer-science-textbook/) | [リポジトリ](https://github.com/itdojp/theoretical-computer-science-textbook)
```

以降の番号は +1 する。

### 説明文を厚くする場合

番号リスト形式を維持したまま、説明文を加えるなら以下を使う。

```markdown
22. 理論計算機科学を読むための数学・証明・アルゴリズム基礎
[書籍を読む](https://itdojp.github.io/theoretical-computer-science-prerequisites-book/) | [リポジトリ](https://github.com/itdojp/theoretical-computer-science-prerequisites-book)
集合・論理・関数・関係・証明技法・漸近記法・擬似コード・グラフ・組合せ・データ構造・形式言語・確率・数論・線形代数・並行モデルを、理論計算機科学教科書に進むための前提として整理するブリッジ教材。
```

### 学習ロードマップ

エンジニアリングマネージャーの `技術理解` にある理論計算機科学教科書の前に追加する。

```diff
-- 技術理解: 基礎分野の概要習得 → 理論計算機科学教科書（理論的背景）
+- 技術理解: 基礎分野の概要習得 → 理論計算機科学を読むための数学・証明・アルゴリズム基礎 → 理論計算機科学教科書（理論的背景）
```

可能なら、専門分野別学習パスに「コンピューターサイエンス理論」を追加する。

```markdown
### コンピューターサイエンス理論

- 前提補強: 理論計算機科学を読むための数学・証明・アルゴリズム基礎
- 本編: 理論計算機科学教科書
- 発展: 圏論によるAIエージェント時代の合成的ソフトウェア設計
```

### ライセンス対象書籍一覧

`## ライセンス` の `対象書籍一覧（リポジトリ）` に追加する。

```markdown
- 理論計算機科学を読むための数学・証明・アルゴリズム基礎 – https://github.com/itdojp/theoretical-computer-science-prerequisites-book
```

## `README.md` の更新

`docs/index.md` と同じ内容を反映する。README が生成物扱いの場合は、プロジェクト側の生成手順に従って再生成する。

## English catalog に追加する場合

英語名:

```text
Mathematics, Proofs, and Algorithms for Reading Theoretical Computer Science
```

掲載文:

```markdown
Mathematics, Proofs, and Algorithms for Reading Theoretical Computer Science
[Read](https://itdojp.github.io/theoretical-computer-science-prerequisites-book/) | [Repository](https://github.com/itdojp/theoretical-computer-science-prerequisites-book)
A Japanese bridge textbook for readers who need prerequisites before studying theoretical computer science: sets, logic, proofs, asymptotic notation, graphs, counting, data structures, formal languages, probability, number theory, linear algebra, and concurrency models.
```

## 変更後の確認

```bash
# knowledge architecture 側
bundle exec jekyll build --source docs --destination _site
# 既存の npm / script がある場合はプロジェクト標準の検証を優先する
```
