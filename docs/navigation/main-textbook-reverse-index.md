# 本体教科書からの逆引き

本体教科書の章を先に選び、必要な前提だけを逆引きするためのページ。

| 本体教科書の章 | 先に確認する前提章 | 確認観点 |
|---|---|---|
| 第1章 数学的基礎 | [第1章](../part-1-core/01-sets-logic.md), [第2章](../part-1-core/02-functions-relations.md), [第3章](../part-1-core/03-proofs.md) | 集合、論理、関数、関係、証明技法を確認する。 |
| 第2章 計算理論の基礎 | [第1章](../part-1-core/01-sets-logic.md), [第2章](../part-1-core/02-functions-relations.md), [第3章](../part-1-core/03-proofs.md), [第5章](../part-1-core/05-pseudocode-recursion.md), [第9章](../part-2-standard/09-formal-language-primer.md) | 問題を言語として表すため、擬似コードと文字列・言語の記法も確認する。 |
| 第3章 形式言語とオートマトン理論 | [第1章](../part-1-core/01-sets-logic.md), [第2章](../part-1-core/02-functions-relations.md), [第3章](../part-1-core/03-proofs.md), [第6章](../part-2-standard/06-graphs-trees.md), [第9章](../part-2-standard/09-formal-language-primer.md) | 遷移関数、到達可能性、構造帰納法、DFA/NFA の記法を確認する。 |
| 第4章 計算可能性理論 | [第1章](../part-1-core/01-sets-logic.md), [第2章](../part-1-core/02-functions-relations.md), [第3章](../part-1-core/03-proofs.md), [第5章](../part-1-core/05-pseudocode-recursion.md), [第9章](../part-2-standard/09-formal-language-primer.md) | 判定問題、計算可能関数、還元を読むために、関数・証明・擬似コードを固める。 |
| 第5章 計算複雑性理論 | [第3章](../part-1-core/03-proofs.md), [第4章](../part-1-core/04-asymptotic-notation.md), [第5章](../part-1-core/05-pseudocode-recursion.md), [第7章](../part-2-standard/07-counting.md), [第9章](../part-2-standard/09-formal-language-primer.md) | 漸近記法、候補数、入力サイズ、言語としての問題表現を確認する。 |
| 第6章 アルゴリズムの数学的解析 | [第3章](../part-1-core/03-proofs.md), [第4章](../part-1-core/04-asymptotic-notation.md), [第5章](../part-1-core/05-pseudocode-recursion.md), [第7章](../part-2-standard/07-counting.md), [第8章](../part-2-standard/08-data-structures.md) | 正しさ証明、計算量、再帰式、データ構造の操作コストを確認する。 |
| 第7章 データ構造の理論 | [第3章](../part-1-core/03-proofs.md), [第4章](../part-1-core/04-asymptotic-notation.md), [第5章](../part-1-core/05-pseudocode-recursion.md), [第6章](../part-2-standard/06-graphs-trees.md), [第8章](../part-2-standard/08-data-structures.md) | 抽象データ型、計算量、木、探索、ループ不変条件を確認する。 |
| 第8章 グラフ理論とネットワーク | [第2章](../part-1-core/02-functions-relations.md), [第3章](../part-1-core/03-proofs.md), [第4章](../part-1-core/04-asymptotic-notation.md), [第6章](../part-2-standard/06-graphs-trees.md), [第7章](../part-2-standard/07-counting.md), [第8章](../part-2-standard/08-data-structures.md) | 関係、到達可能性、BFS/DFS、数え上げ、データ構造を確認する。 |
| 第9章 論理と形式的手法 | [第1章](../part-1-core/01-sets-logic.md), [第2章](../part-1-core/02-functions-relations.md), [第3章](../part-1-core/03-proofs.md), [第13章](../part-3-extended/13-concurrency-models.md) | 述語論理、関係、証明、状態遷移・安全性・活性を確認する。 |
| 第10章 情報理論 | [第7章](../part-2-standard/07-counting.md), [第10章](../part-3-extended/10-probability.md), [第12章](../part-3-extended/12-linear-algebra.md) | 数え上げ、確率、期待値、線形符号、Hamming距離を確認する。 |
| 第11章 暗号理論 | [第4章](../part-1-core/04-asymptotic-notation.md), [第7章](../part-2-standard/07-counting.md), [第10章](../part-3-extended/10-probability.md), [第11章](../part-3-extended/11-number-theory-algebra.md) | 計算困難性、確率、鍵空間、合同算術、群・体の入口を確認する。 |
| 第12章 並行計算の理論 | [第2章](../part-1-core/02-functions-relations.md), [第3章](../part-1-core/03-proofs.md), [第6章](../part-2-standard/06-graphs-trees.md), [第10章](../part-3-extended/10-probability.md), [第12章](../part-3-extended/12-linear-algebra.md), [第13章](../part-3-extended/13-concurrency-models.md) | 関係、グラフ、確率との区別、線形代数、状態遷移、合意問題を確認する。 |


## 運用ルール

- 本体教科書を第1章から順に読む場合は、Core → Standard → Extended の順で進める。
- 特定章だけを読む場合は、上表の前提章だけを先に確認する。
- 章を読んで詰まった場合は、該当する前提章の「この章で使う記号」と章末確認チェックへ戻る。
- 情報理論・暗号・並行計算は Extended を省略すると読解コストが上がる。

## readiness checklist への接続

実際に本体へ進む前には、[本体教科書 readiness checklist](../assessment/main-textbook-readiness.md) で章別に判定する。
