from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class CounterState:
    x: int
    p_done: bool
    q_done: bool


def next_states(state: CounterState) -> set[CounterState]:
    """A tiny nondeterministic transition system.

    Process P and Q each increment x once. Each increment is modeled as atomic here.
    The nondeterminism is only the order of P and Q.
    """
    result: set[CounterState] = set()
    if not state.p_done:
        result.add(CounterState(state.x + 1, True, state.q_done))
    if not state.q_done:
        result.add(CounterState(state.x + 1, state.p_done, True))
    return result


def reachable(initial: CounterState) -> set[CounterState]:
    seen = {initial}
    q: deque[CounterState] = deque([initial])
    while q:
        s = q.popleft()
        for t in next_states(s):
            if t not in seen:
                seen.add(t)
                q.append(t)
    return seen


def violates_safety(initial: CounterState, bad: Callable[[CounterState], bool]) -> CounterState | None:
    for state in reachable(initial):
        if bad(state):
            return state
    return None


if __name__ == "__main__":
    init = CounterState(0, False, False)
    states = reachable(init)
    print("reachable states:")
    for s in sorted(states, key=lambda z: (z.p_done, z.q_done, z.x)):
        print(s)
    print("bad x > 2:", violates_safety(init, lambda s: s.x > 2))
