from __future__ import annotations

import random
from collections import Counter


def coin_tosses(n: int, seed: int = 0) -> dict[str, float]:
    rng = random.Random(seed)
    counts = Counter("H" if rng.random() < 0.5 else "T" for _ in range(n))
    return {k: counts[k] / n for k in ["H", "T"]}


def conditional_probability_demo(n: int, seed: int = 0) -> float:
    """Estimate P(first die is 6 | sum is at least 10)."""
    rng = random.Random(seed)
    condition = 0
    event_and_condition = 0
    for _ in range(n):
        a = rng.randint(1, 6)
        b = rng.randint(1, 6)
        if a + b >= 10:
            condition += 1
            if a == 6:
                event_and_condition += 1
    if condition == 0:
        raise RuntimeError("condition did not occur")
    return event_and_condition / condition


if __name__ == "__main__":
    print("coin tosses:", coin_tosses(10_000, seed=1))
    print("conditional estimate:", conditional_probability_demo(50_000, seed=1))
