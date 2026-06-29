# 第5章 擬似コードと再帰

!!! info "章間ナビゲーション"
    - 前: [第4章 漸近記法](04-asymptotic-notation.md)
    - 次: [第6章 グラフと木](../part-2-standard/06-graphs-trees.md)
    - 章別マップ: [章間リンクマップ](../navigation/chapter-link-map.md)
    - 用語確認: [用語索引](../reference/glossary.md) / [記号索引](../reference/symbol-index.md)
    - 到達判定: [章末確認チェック](../assessment/chapter-exit-checks.md)


## この章で使う記号

| 記号 | 意味 |
|---|---|
| `x := v` | `x` に `v` を代入する擬似コード記法 |
| `if / else` | 条件分岐 |
| `while` / `for` | 反復 |
| `return` | 関数の戻り値 |
| `A[i]` | 配列 `A` の `i` 番目の要素 |
| `len(A)` | 列や配列の長さ |
| `call f(x)` | 関数呼び出し |


## この章で解消する詰まりどころ

理論計算機科学では、特定のプログラミング言語ではなく、擬似コードや抽象機械でアルゴリズムを記述します。重要なのは、文法を覚えることではなく、状態変化と制御構造を追えることです。

この章の目的は、次の状態を作ることです。

- 擬似コードの代入、分岐、ループを正しく読める。
- 配列、リスト、辞書、集合を抽象データ型として扱える。
- 関数呼び出しと戻り値を追跡できる。
- 再帰の停止条件と再帰呼び出しを説明できる。
- 再帰的アルゴリズムの正しさを帰納法と接続できる。
- 線形探索、二分探索、BFS/DFSへの準備ができる。

## 本体教科書のどこで使うか

- 第2章 計算理論の基礎
- 第4章 計算可能性理論
- 第6章 アルゴリズムの数学的解析
- 第7章 データ構造の理論
- 第8章 グラフ理論とネットワーク

---

## 1. 擬似コードの位置づけ

擬似コードは、特定の言語に依存しないアルゴリズム記述です。

Python, Java, C のような実言語では、型、構文、標準ライブラリ、実行環境を考慮します。擬似コードでは、それらを省略し、アルゴリズムの本質だけを書きます。

例:

```text
LinearSearch(A, x):
    for i = 0 to len(A)-1:
        if A[i] == x:
            return i
    return NOT_FOUND
```

これは Python ではありませんが、十分に意味が分かります。

---

## 2. 実行状態

プログラムの実行状態は、変数の値と現在実行している位置で決まります。

例:

```text
x = 1
y = 2
x = x + y
```

実行後の状態は、

```text
x = 3
y = 2
```

です。代入 `x = x + y` は、右辺の現在値を評価してから左辺に代入します。

---

## 3. 条件分岐

```text
if condition:
    A
else:
    B
```

`condition` が真なら `A` を実行し、偽なら `B` を実行します。

例:

```text
Abs(x):
    if x >= 0:
        return x
    else:
        return -x
```

この関数は、`x` が非負ならそのまま返し、負なら符号を反転して返します。

---

## 4. ループ

### for ループ

```text
for i = 1 to n:
    body
```

典型的には、`i=1,2,...,n` の順に `body` を実行します。

### while ループ

```text
while condition:
    body
```

`condition` が真である限り `body` を繰り返します。

while ループでは、次の2点を確認します。

1. ループ条件がいつか偽になるか。
2. 各反復で状態がどう変化するか。

例:

```text
i = n
while i > 1:
    i = floor(i / 2)
```

`i` は正の整数で、各回で小さくなります。したがって停止します。

---

## 5. 配列と添字

本教材では、配列 `A` の添字は原則として `0` から始めます。

```text
A[0], A[1], ..., A[len(A)-1]
```

ただし、数学的説明では `1` から始めることもあります。重要なのは、範囲を明示することです。

### よくある範囲

| 表記 | 意味 |
|---|---|
| `0 <= i < n` | `0` から `n-1` まで |
| `1 <= i <= n` | `1` から `n` まで |
| `A[l..r]` | `l` から `r` までの部分配列。閉区間か半開区間かは文脈で明示する |

---

## 6. 関数

関数は、入力を受け取り、処理を行い、値を返します。

```text
Square(x):
    return x * x
```

呼び出し:

```text
Square(5) = 25
```

関数の仕様は、次の形で書きます。

```text
入力: x は整数
出力: x^2
前提条件: なし
事後条件: 戻り値 y は y=x^2 を満たす
```

理論計算機科学では、アルゴリズムを「入力から出力への関数」として見ることがあります。この見方に慣れておくと、計算可能性や複雑性の章に入りやすくなります。

---

## 7. 再帰

再帰関数は、自分自身を呼び出す関数です。

例: 階乗

```text
Fact(n):
    if n == 0:
        return 1
    return n * Fact(n-1)
```

`Fact(4)` の展開:

```text
Fact(4)
= 4 * Fact(3)
= 4 * 3 * Fact(2)
= 4 * 3 * 2 * Fact(1)
= 4 * 3 * 2 * 1 * Fact(0)
= 4 * 3 * 2 * 1 * 1
= 24
```

再帰には必ず次が必要です。

1. **基底ケース**: それ以上再帰しない場合。
2. **再帰ケース**: より小さい、またはより単純な問題に帰着する場合。

階乗では、`n==0` が基底ケース、`Fact(n-1)` が再帰ケースです。

---

## 8. 呼び出しスタック

再帰呼び出しでは、各呼び出しが自分のローカル変数と戻り先を持ちます。

`Fact(3)` の実行では、概念的に次の呼び出しが積まれます。

```text
Fact(3)
  waits for Fact(2)
    waits for Fact(1)
      waits for Fact(0)
```

`Fact(0)` が返ると、逆順に計算が戻ります。

```text
Fact(0) returns 1
Fact(1) returns 1 * 1 = 1
Fact(2) returns 2 * 1 = 2
Fact(3) returns 3 * 2 = 6
```

---

## 9. 停止性

再帰関数が正しいためには、正しい値を返すだけでなく、停止する必要があります。

停止性を示す典型的な方法は、自然数値の尺度が各再帰呼び出しで小さくなることを示すことです。

階乗では、尺度は `n` です。

```text
Fact(n) は n>0 のとき Fact(n-1) を呼ぶ。
n-1 < n であり、n は自然数なので、いつか 0 に到達する。
したがって停止する。
```

このような尺度を **variant** または **ranking function** と呼ぶことがあります。

---

## 10. 再帰と帰納法

再帰関数の正しさは、帰納法で証明するのが自然です。

例:

```text
Fact(n) は n! を返す。
```

基底部:

```text
n=0 のとき、Fact(0)=1。これは 0! = 1 と一致する。
```

帰納ステップ:

```text
Fact(k) が k! を返すと仮定する。
Fact(k+1) は (k+1) * Fact(k) を返す。
帰納法の仮定より Fact(k)=k! なので、Fact(k+1) は (k+1)k! = (k+1)! を返す。
```

したがって、すべての `n` について `Fact(n)` は `n!` を返します。

---

## 11. 線形探索

仕様:

```text
入力: 配列 A, 探す値 x
出力: x が A に含まれるなら、その添字の1つ。含まれないなら NOT_FOUND。
```

擬似コード:

```text
LinearSearch(A, x):
    for i = 0 to len(A)-1:
        if A[i] == x:
            return i
    return NOT_FOUND
```

時間計算量:

- 最悪の場合、配列全体を調べる。
- したがって `Θ(n)`。

正しさ:

- `return i` する場合、実際に `A[i]==x` なので正しい。
- 最後まで見つからない場合、全要素を確認済みなので `NOT_FOUND` は正しい。

---

## 12. 二分探索

二分探索は、ソート済み配列で使えます。

仕様:

```text
入力: 昇順ソート済み配列 A, 探す値 x
出力: x が A に含まれるなら、その添字。含まれないなら NOT_FOUND。
前提条件: A は昇順にソートされている。
```

擬似コード:

```text
BinarySearch(A, x):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = floor((left + right) / 2)
        if A[mid] == x:
            return mid
        if A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return NOT_FOUND
```

### 不変条件

各反復の開始時点で、もし `x` が配列に存在するなら、`x` は範囲 `A[left..right]` の中に存在します。

初期化:

```text
最初は left=0, right=len(A)-1 なので、探索範囲は配列全体である。
```

保存:

```text
A[mid] < x の場合、配列は昇順なので、mid 以下には x は存在しない。
したがって left=mid+1 としても、存在し得る範囲は保たれる。
A[mid] > x の場合も同様に、right=mid-1 とできる。
```

終了:

```text
left > right になった場合、探索範囲は空である。
不変条件より、x は配列に存在しない。
```

計算量:

各反復で探索範囲はほぼ半分になるため、時間計算量は `Θ(log n)` です。

---

## 13. BFS と DFS の入口

グラフ探索では、次の2つが基本です。

- BFS: キューを使い、始点から近い順に探索する。
- DFS: スタックまたは再帰を使い、行けるところまで深く進む。

この章では詳細実装までは扱いません。第6章で扱います。ただし、どちらも次のパターンを持ちます。

```text
visited = empty set
worklist = initial vertices
while worklist is not empty:
    v = remove one vertex from worklist
    if v is not in visited:
        add v to visited
        add neighbors of v to worklist
```

`worklist` がキューなら BFS、スタックなら DFS です。

---

## 14. 正しさと計算量は別の主張

アルゴリズムについては、少なくとも次の2つを別々に示します。

1. **正しさ**: 返す答えが仕様を満たす。
2. **計算量**: 実行時間やメモリ使用量がどの程度か。

正しいが遅いアルゴリズムもあります。速いが間違った答えを返すものはアルゴリズムとして不適切です。

例:

```text
配列内に x が存在するかを調べる問題
```

- 全探索は正しいが `Θ(n)`。
- ソート済みなら二分探索が使え、`Θ(log n)`。
- ソートされていない配列に二分探索を使うと、速いかもしれないが正しくない。

---

## 15. Python 実装例

### 線形探索

```python
def linear_search(a, x):
    for i, value in enumerate(a):
        if value == x:
            return i
    return None
```

### 二分探索

```python
def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        if a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return None
```

### 再帰階乗

```python
def fact(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * fact(n - 1)
```

---

## 16. 練習問題

1. 次のコードの実行後の `x,y` を答えよ。

```text
x = 1
y = 3
x = x + y
y = x - y
```

2. `while` ループが停止することを説明せよ。

```text
i = n
while i > 0:
    i = i - 1
```

3. `Fact(5)` の呼び出し列を書け。
4. 再帰版 `Fact(n)` が停止する理由を書け。
5. 二分探索が使えるための前提条件を書け。
6. 二分探索の不変条件を書け。
7. ソートされていない配列に二分探索を使うと正しくない理由を例で説明せよ。
8. 線形探索の正しさと計算量を分けて説明せよ。


---

## 次に読む章

- 通常ルート: [第6章 グラフと木](../part-2-standard/06-graphs-trees.md)
- 演習: [Core 演習](../exercises/pseudocode-recursion-drills.md)
- 解答: [演習解答](../exercises/solutions.md)
- 図表: [関連図表](../visual/proof-and-logic-diagrams.md)
- 実装確認: [Python実装ノート](../python/algorithm-snippets.md)
- 全体導線: [学習チェックリスト](../assessment/learning-checklists.md)
