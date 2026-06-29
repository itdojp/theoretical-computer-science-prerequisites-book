from __future__ import annotations

import math
import pytest

from bfs_layers import bfs_distances, reconstruct_path, sample_graph
from dfa_simulator import DFA, even_number_of_ones_dfa
from hamming_distance import hamming_distance, minimum_distance, nearest_codewords
from modular_arithmetic import gcd, mod_inverse, toy_rsa_roundtrip
from probability_experiments import coin_tosses, conditional_probability_demo
from recursion_trace import factorial, factorial_trace
from state_transition import CounterState, reachable, violates_safety
from union_find import UnionFind


def test_factorial_and_trace() -> None:
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial_trace(3)[0] == "call factorial(3)"
    with pytest.raises(ValueError):
        factorial(-1)


def test_bfs_layers() -> None:
    graph = sample_graph()
    dist, parent = bfs_distances(graph, "s")
    assert dist["s"] == 0
    assert dist["g"] == 3
    assert reconstruct_path(parent, "g")[0] == "s"
    assert reconstruct_path(parent, "missing") == []
    with pytest.raises(KeyError):
        bfs_distances(graph, "missing")


def test_union_find() -> None:
    uf = UnionFind([1, 2, 3, 4])
    uf.union(1, 2)
    uf.union(3, 4)
    assert uf.connected(1, 2)
    assert not uf.connected(1, 3)
    uf.union(2, 4)
    assert uf.connected(1, 3)
    with pytest.raises(KeyError):
        uf.find(99)


def test_dfa_simulator() -> None:
    dfa = even_number_of_ones_dfa()
    assert dfa.run("")[0]
    assert dfa.run("00")[0]
    assert not dfa.run("1")[0]
    assert dfa.run("101")[0]
    assert not dfa.run("1011")[0]
    with pytest.raises(ValueError):
        dfa.run("2")

    bad = DFA(states={"q"}, alphabet={"0"}, transition={}, start="q", accepting=set())
    with pytest.raises(ValueError):
        bad.validate()


def test_hamming_distance() -> None:
    assert hamming_distance("1011", "1110") == 2
    assert minimum_distance({"000", "111"}) == 3
    assert nearest_codewords("001", {"000", "111"}) == (1, ["000"])
    with pytest.raises(ValueError):
        hamming_distance("0", "00")


def test_modular_arithmetic() -> None:
    assert gcd(84, 30) == 6
    assert mod_inverse(7, 26) == 15
    with pytest.raises(ValueError):
        mod_inverse(2, 6)
    cipher, plain = toy_rsa_roundtrip(12)
    assert cipher != 12
    assert plain == 12


def test_probability_experiments() -> None:
    toss = coin_tosses(1000, seed=1)
    assert set(toss) == {"H", "T"}
    assert math.isclose(toss["H"] + toss["T"], 1.0)
    estimate = conditional_probability_demo(5000, seed=1)
    assert 0.0 <= estimate <= 1.0


def test_state_transition() -> None:
    init = CounterState(0, False, False)
    states = reachable(init)
    assert CounterState(2, True, True) in states
    assert violates_safety(init, lambda s: s.x > 2) is None
    assert violates_safety(init, lambda s: s.x == 1) is not None
