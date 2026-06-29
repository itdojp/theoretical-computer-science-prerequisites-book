# Python実装ノート: 確率・数論・線形代数・状態遷移

## 確率実験

対象ファイル:

```text
examples/python/probability_experiments.py
```

乱数実験は直観の確認には有効だが、証明の代替にはならない。乱数を使うときは seed を固定し、理論値と実験値を区別する。

## 合同算術

対象ファイル:

```text
examples/python/modular_arithmetic.py
```

`a ≡ b (mod n)` は、`a` と `b` が `n` で割った余りを共有することを意味する。Python の `%` 演算子で確認できるが、逆元や gcd は定義から理解する必要がある。

## Hamming距離

対象ファイル:

```text
examples/python/hamming_distance.py
```

Hamming距離は、同じ長さの語を位置ごとに比較して、異なる位置を数える。

```python
def hamming_distance(x: str, y: str) -> int:
    if len(x) != len(y):
        raise ValueError("same length required")
    return sum(a != b for a, b in zip(x, y))
```

## 状態遷移系

対象ファイル:

```text
examples/python/state_transition.py
```

状態遷移系では、次状態が一つとは限らない。非決定性は `set` で表せる。

```python
next_states: dict[State, set[State]]
```

safety の検査は「到達可能状態の中に悪い状態が存在しないこと」を確認する問題として書ける。
