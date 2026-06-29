# Python実装ノート: 形式言語とオートマトン

対象ファイル:

```text
examples/python/dfa_simulator.py
```

## DFA の実装

DFA は5つ組で定義する。

```text
(Q, Σ, δ, q0, F)
```

Python では次のように表せる。

```python
states = {"even", "odd"}
alphabet = {"0", "1"}
transition = {
    ("even", "0"): "even",
    ("even", "1"): "odd",
    ("odd", "0"): "odd",
    ("odd", "1"): "even",
}
start = "even"
accepting = {"even"}
```

## 全域性の検査

DFA の遷移関数は、すべての状態と入力記号の組に対して定義されていなければならない。

```python
for q in states:
    for a in alphabet:
        assert (q, a) in transition
```

この検査を省略すると、実装は「一部の入力で落ちるプログラム」になり、形式的な DFA ではなくなる。

## 読解ポイント

| 観点 | 確認内容 |
|---|---|
| 状態の意味 | 何を記憶しているか |
| 遷移の意味 | 入力記号で記憶がどう変わるか |
| 受理条件 | 入力をすべて読んだ後、どの状態なら受理か |
| 不変条件 | 任意の接頭辞を読んだ後に状態が何を表すか |

DFA の正しさ証明は、入力文字列の長さに関する帰納法で書ける。
