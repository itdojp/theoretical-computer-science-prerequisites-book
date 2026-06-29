# 課題提出フォーマット

## 目的

このページは、演習・レビュー問題・ミニプロジェクトを提出する際の標準フォーマットを定めます。採点者が答案を読み、定義・証明・実装・再現手順を確認できることを優先します。

## 推奨提出単位

| 課題種別 | 推奨形式 |
|---|---|
| 前提診断 | Markdown または CSV |
| 章別レビュー問題 | Markdown |
| 証明問題 | Markdown または PDF化可能なMarkdown |
| 計算量解析 | Markdown、必要なら擬似コード付き |
| Python実装 | Gitリポジトリまたは単一ディレクトリ |
| ミニプロジェクト | Gitリポジトリ |
| 統合到達確認テスト | Markdown |

## ディレクトリ構成

```text
submission/
  README.md
  answers/
    chapter-01.md
    chapter-02.md
    integrated-readiness-test.md
  src/
    project_code.py
  tests/
    test_project_code.py
  notes/
    review-response.md
```

小規模提出では `README.md` だけでも構いません。ただし、ミニプロジェクトでは `src/` と `tests/` を分けます。

## READMEに含める項目

```text
# 提出物タイトル

## 受講者情報

- learner_id:
- cohort_id:
- 提出日:
- 対象章:

## 対象課題

- 課題名:
- 対象ファイル:
- 参照した教材ページ:

## 実行方法

```bash
python -m pytest
python src/project_code.py
```

## 自己評価

- 定義を使って説明できた点:
- 不明点:
- レビューしてほしい点:

## AI利用の有無

- 利用有無:
- 利用した場合の用途:
- 自分で検証した内容:
```

## 証明問題の書き方

証明答案は、次の構造にします。

```text
主張:
仮定:
示すべきこと:
使う定義:
証明:
結論:
```

悪い答案は、例をいくつか確認して終わるものです。良い答案は、任意の対象について定義から結論へ進みます。

## 計算量問題の書き方

```text
対象コード:
入力サイズの定義:
支配的な操作:
実行回数:
計算量:
根拠:
```

`O(n)` と書くだけでは不十分です。何を1操作として数えたかを明示します。

## 実装課題の書き方

実装課題では、以下を必ず含めます。

- 仕様
- 入力例
- 出力例
- 実装方針
- 境界ケース
- テスト
- 実行方法

Pythonコードでは、少なくとも主要関数に型ヒントを付けます。

```python
def hamming_distance(x: str, y: str) -> int:
    if len(x) != len(y):
        raise ValueError("length mismatch")
    return sum(a != b for a, b in zip(x, y))
```

## レビューコメントへの対応

再提出時は、レビューコメントを消さず、対応内容を別ファイルに残します。

```text
## レビュー対応

### 指摘1

指摘内容:
対応内容:
修正ファイル:
未解決の場合の理由:
```

## 提出テンプレート

テンプレートは [課題提出テンプレート](../forms/assignment-submission.md) を使います。
