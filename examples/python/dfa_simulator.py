from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable

State = Hashable
Symbol = str


@dataclass(frozen=True)
class DFA:
    states: set[State]
    alphabet: set[Symbol]
    transition: dict[tuple[State, Symbol], State]
    start: State
    accepting: set[State]

    def validate(self) -> None:
        if self.start not in self.states:
            raise ValueError("start state is not in states")
        if not self.accepting <= self.states:
            raise ValueError("accepting states must be subset of states")
        for q in self.states:
            for a in self.alphabet:
                if (q, a) not in self.transition:
                    raise ValueError(f"missing transition: {q!r}, {a!r}")
                if self.transition[(q, a)] not in self.states:
                    raise ValueError("transition target is not in states")

    def run(self, word: str) -> tuple[bool, list[State]]:
        self.validate()
        state = self.start
        trace: list[State] = [state]
        for ch in word:
            if ch not in self.alphabet:
                raise ValueError(f"symbol not in alphabet: {ch!r}")
            state = self.transition[(state, ch)]
            trace.append(state)
        return state in self.accepting, trace


def even_number_of_ones_dfa() -> DFA:
    return DFA(
        states={"even", "odd"},
        alphabet={"0", "1"},
        transition={
            ("even", "0"): "even",
            ("even", "1"): "odd",
            ("odd", "0"): "odd",
            ("odd", "1"): "even",
        },
        start="even",
        accepting={"even"},
    )


if __name__ == "__main__":
    dfa = even_number_of_ones_dfa()
    for word in ["", "0", "1", "101", "1011"]:
        accepted, trace = dfa.run(word)
        print(word or "ε", accepted, trace)
