# 用語索引

理論計算機科学教科書の前提補強で頻出する用語を、章への逆リンク付きで整理する。

| 用語 | 意味 | 関連章 |
|---|---|---|
| 集合 | 対象をまとめたもの。理論では問題、状態、入力、言語などを集合として表す。 | [第1章 集合と論理](../part-1-core/01-sets-logic.md) |
| 要素 | 集合に含まれる個々の対象。 | [第1章 集合と論理](../part-1-core/01-sets-logic.md) |
| 部分集合 | `A` のすべての要素が `B` に含まれるとき、`A ⊆ B` と書く。 | [第1章 集合と論理](../part-1-core/01-sets-logic.md) |
| 命題 | 真または偽が定まる文。 | [第1章 集合と論理](../part-1-core/01-sets-logic.md) |
| 述語 | 変数に値を入れると命題になる式。 | [第1章 集合と論理](../part-1-core/01-sets-logic.md) |
| 量化記号 | `∀` と `∃`。全称と存在を表す。 | [第1章 集合と論理](../part-1-core/01-sets-logic.md) |
| 含意 | `P → Q`。`P` が真なら `Q` が真であるという主張。 | [第1章 集合と論理](../part-1-core/01-sets-logic.md) |
| 対偶 | `P → Q` に対する `¬Q → ¬P`。元の命題と同値。 | [第1章 集合と論理](../part-1-core/01-sets-logic.md) |
| 関数 | 定義域の各要素に、終域の要素をちょうど1つ対応させる規則。 | [第2章 関数と関係](../part-1-core/02-functions-relations.md) |
| 単射 | 異なる入力が異なる出力に写る関数。 | [第2章 関数と関係](../part-1-core/02-functions-relations.md) |
| 全射 | 終域のすべての要素が少なくとも1つの入力から写される関数。 | [第2章 関数と関係](../part-1-core/02-functions-relations.md) |
| 全単射 | 単射かつ全射の関数。 | [第2章 関数と関係](../part-1-core/02-functions-relations.md) |
| 二項関係 | 2つの要素の間に成り立つ関係。集合としては直積の部分集合。 | [第2章 関数と関係](../part-1-core/02-functions-relations.md) |
| 同値関係 | 反射律・対称律・推移律を満たす関係。分類を作る。 | [第2章 関数と関係](../part-1-core/02-functions-relations.md) |
| 半順序 | 反射律・反対称律・推移律を満たす順序。すべての要素が比較可能とは限らない。 | [第2章 関数と関係](../part-1-core/02-functions-relations.md) |
| 直接証明 | 仮定から結論をそのまま導く証明。 | [第3章 証明技法](../part-1-core/03-proofs.md) |
| 背理法 | 結論の否定を仮定して矛盾を導く証明。 | [第3章 証明技法](../part-1-core/03-proofs.md) |
| 反例 | 普遍命題が偽であることを示す具体例。 | [第3章 証明技法](../part-1-core/03-proofs.md) |
| 数学的帰納法 | 基底部と帰納ステップで自然数に関する命題を証明する技法。 | [第3章 証明技法](../part-1-core/03-proofs.md) |
| 構造帰納法 | 文字列、木、式など再帰的に定義された対象に対する帰納法。 | [第3章 証明技法](../part-1-core/03-proofs.md) |
| 不変条件 | ループや状態遷移の各時点で保たれる性質。 | [第3章 証明技法](../part-1-core/03-proofs.md) |
| O記法 | 関数の漸近的上界を表す記法。 | [第4章 漸近記法](../part-1-core/04-asymptotic-notation.md) |
| Ω記法 | 関数の漸近的下界を表す記法。 | [第4章 漸近記法](../part-1-core/04-asymptotic-notation.md) |
| Θ記法 | 漸近的に同じ増加率を表す記法。 | [第4章 漸近記法](../part-1-core/04-asymptotic-notation.md) |
| 再帰式 | 入力サイズ `n` の計算量を、より小さい入力サイズの計算量で表す式。 | [第4章 漸近記法](../part-1-core/04-asymptotic-notation.md) |
| 擬似コード | 特定の言語仕様を省き、アルゴリズムの本質だけを書く記法。 | [第5章 擬似コードと再帰](../part-1-core/05-pseudocode-recursion.md) |
| 再帰 | 関数や定義が自分自身を参照する構造。 | [第5章 擬似コードと再帰](../part-1-core/05-pseudocode-recursion.md) |
| 呼び出しスタック | 関数呼び出しの途中状態を積む実行時構造。 | [第5章 擬似コードと再帰](../part-1-core/05-pseudocode-recursion.md) |
| グラフ | 頂点集合と辺集合からなる構造。 | [第6章 グラフと木](../part-2-standard/06-graphs-trees.md) |
| 木 | 連結で閉路を持たない無向グラフ。 | [第6章 グラフと木](../part-2-standard/06-graphs-trees.md) |
| DAG | 有向非巡回グラフ。依存関係や順序制約を表す。 | [第6章 グラフと木](../part-2-standard/06-graphs-trees.md) |
| BFS | 始点から距離の近い順に探索する幅優先探索。 | [第6章 グラフと木](../part-2-standard/06-graphs-trees.md) |
| DFS | 深く進んでから戻る深さ優先探索。 | [第6章 グラフと木](../part-2-standard/06-graphs-trees.md) |
| トポロジカルソート | DAGの辺の向きに矛盾しない頂点の順序付け。 | [第6章 グラフと木](../part-2-standard/06-graphs-trees.md) |
| 和の法則 | 重ならない選択肢の総数を足し合わせる規則。 | [第7章 組合せと数え上げ](../part-2-standard/07-counting.md) |
| 積の法則 | 独立した段階的選択の総数を掛け合わせる規則。 | [第7章 組合せと数え上げ](../part-2-standard/07-counting.md) |
| 鳩ノ巣原理 | 箱より多いものを入れると、少なくとも1つの箱に2つ以上入るという原理。 | [第7章 組合せと数え上げ](../part-2-standard/07-counting.md) |
| 包除原理 | 重なりを補正して集合の和の大きさを求める原理。 | [第7章 組合せと数え上げ](../part-2-standard/07-counting.md) |
| 抽象データ型 | 操作の仕様を定め、実装方法は分離する考え方。 | [第8章 データ構造と基本アルゴリズム](../part-2-standard/08-data-structures.md) |
| スタック | 後入れ先出しのデータ構造。 | [第8章 データ構造と基本アルゴリズム](../part-2-standard/08-data-structures.md) |
| キュー | 先入れ先出しのデータ構造。 | [第8章 データ構造と基本アルゴリズム](../part-2-standard/08-data-structures.md) |
| ヒープ | 最小値または最大値を効率よく取り出すための木構造。 | [第8章 データ構造と基本アルゴリズム](../part-2-standard/08-data-structures.md) |
| ハッシュ表 | キーをハッシュ値に変換して高速検索するデータ構造。 | [第8章 データ構造と基本アルゴリズム](../part-2-standard/08-data-structures.md) |
| Union-Find | 互いに素な集合族の併合と代表元検索を効率よく行うデータ構造。 | [第8章 データ構造と基本アルゴリズム](../part-2-standard/08-data-structures.md) |
| アルファベット | 形式言語で使う有限個の記号集合。 | [第9章 形式言語の入口](../part-2-standard/09-formal-language-primer.md) |
| 文字列 | アルファベット上の有限列。 | [第9章 形式言語の入口](../part-2-standard/09-formal-language-primer.md) |
| 空文字列 | 長さ0の文字列。通常 `ε` と書く。 | [第9章 形式言語の入口](../part-2-standard/09-formal-language-primer.md) |
| 言語 | 文字列の集合。 | [第9章 形式言語の入口](../part-2-standard/09-formal-language-primer.md) |
| DFA | 決定性有限オートマトン。各状態と入力記号に対して次状態が一意に定まる。 | [第9章 形式言語の入口](../part-2-standard/09-formal-language-primer.md) |
| NFA | 非決定性有限オートマトン。複数の遷移候補や ε 遷移を許す。 | [第9章 形式言語の入口](../part-2-standard/09-formal-language-primer.md) |
| 標本空間 | 確率実験で起こり得る結果全体の集合。 | [第10章 確率の基礎](../part-3-extended/10-probability.md) |
| 事象 | 標本空間の部分集合。 | [第10章 確率の基礎](../part-3-extended/10-probability.md) |
| 条件付き確率 | ある事象が起きた条件下での確率。 | [第10章 確率の基礎](../part-3-extended/10-probability.md) |
| 独立性 | 一方の事象の発生が他方の確率を変えない性質。 | [第10章 確率の基礎](../part-3-extended/10-probability.md) |
| 確率変数 | 標本空間の結果を数値に写す関数。 | [第10章 確率の基礎](../part-3-extended/10-probability.md) |
| 期待値 | 確率変数の平均的な値。 | [第10章 確率の基礎](../part-3-extended/10-probability.md) |
| 最大公約数 | 2つの整数をともに割り切る最大の正整数。 | [第11章 数論・代数の基礎](../part-3-extended/11-number-theory-algebra.md) |
| 合同算術 | 整数を法 `n` の剰余で扱う算術。 | [第11章 数論・代数の基礎](../part-3-extended/11-number-theory-algebra.md) |
| 逆元 | 積が単位元になる相手。剰余計算では `ax ≡ 1 (mod n)` を満たす `x`。 | [第11章 数論・代数の基礎](../part-3-extended/11-number-theory-algebra.md) |
| 群 | 閉性、結合律、単位元、逆元を満たす代数構造。 | [第11章 数論・代数の基礎](../part-3-extended/11-number-theory-algebra.md) |
| 体 | 加減乗除ができる代数構造。ただし0での除算を除く。 | [第11章 数論・代数の基礎](../part-3-extended/11-number-theory-algebra.md) |
| ベクトル | 数を並べたもの。 | [第12章 線形代数の最小限](../part-3-extended/12-linear-algebra.md) |
| 行列 | 数を長方形に並べたもの。 | [第12章 線形代数の最小限](../part-3-extended/12-linear-algebra.md) |
| ランク | 行列の独立な行または列の数。 | [第12章 線形代数の最小限](../part-3-extended/12-linear-algebra.md) |
| 2元体 | 0と1だけを持ち、mod 2で計算する体。 | [第12章 線形代数の最小限](../part-3-extended/12-linear-algebra.md) |
| Hamming距離 | 同じ長さの文字列で異なる位置の数。 | [第12章 線形代数の最小限](../part-3-extended/12-linear-algebra.md) |
| 状態遷移 | ある状態から別の状態へ移ること。 | [第13章 並行性と形式モデルの入口](../part-3-extended/13-concurrency-models.md) |
| 非決定性 | 同じ状態から複数の次状態があり得ること。ランダムとは異なる。 | [第13章 並行性と形式モデルの入口](../part-3-extended/13-concurrency-models.md) |
| 安全性 | 悪いことが起きないという性質。 | [第13章 並行性と形式モデルの入口](../part-3-extended/13-concurrency-models.md) |
| 活性 | 良いことがいつか起きるという性質。 | [第13章 並行性と形式モデルの入口](../part-3-extended/13-concurrency-models.md) |
| happens-before | 並行実行における因果順序を表す関係。 | [第13章 並行性と形式モデルの入口](../part-3-extended/13-concurrency-models.md) |
| 合意問題 | 複数プロセスが同じ値に合意する問題。 | [第13章 並行性と形式モデルの入口](../part-3-extended/13-concurrency-models.md) |
