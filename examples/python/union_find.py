from __future__ import annotations

from typing import Hashable


class UnionFind:
    """Union-Find with path compression and union by size."""

    def __init__(self, elements: list[Hashable]):
        self.parent: dict[Hashable, Hashable] = {x: x for x in elements}
        self.size: dict[Hashable, int] = {x: 1 for x in elements}

    def find(self, x: Hashable) -> Hashable:
        if x not in self.parent:
            raise KeyError(x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: Hashable, y: Hashable) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]

    def connected(self, x: Hashable, y: Hashable) -> bool:
        return self.find(x) == self.find(y)

    def components(self) -> dict[Hashable, set[Hashable]]:
        result: dict[Hashable, set[Hashable]] = {}
        for x in self.parent:
            result.setdefault(self.find(x), set()).add(x)
        return result


if __name__ == "__main__":
    uf = UnionFind([1, 2, 3, 4, 5])
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(2, 4)
    print(uf.components())
    print("connected(1, 4):", uf.connected(1, 4))
    print("connected(1, 5):", uf.connected(1, 5))
