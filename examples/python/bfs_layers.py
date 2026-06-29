from __future__ import annotations

from collections import deque
from typing import TypeVar

V = TypeVar("V")
Graph = dict[V, set[V]]


def bfs_distances(graph: Graph[V], start: V) -> tuple[dict[V, int], dict[V, V | None]]:
    """Compute BFS distances and parent pointers from start."""
    if start not in graph:
        raise KeyError("start vertex is not in graph")
    distance: dict[V, int] = {start: 0}
    parent: dict[V, V | None] = {start: None}
    q: deque[V] = deque([start])
    while q:
        v = q.popleft()
        for w in graph.get(v, set()):
            if w not in distance:
                distance[w] = distance[v] + 1
                parent[w] = v
                q.append(w)
    return distance, parent


def reconstruct_path(parent: dict[V, V | None], target: V) -> list[V]:
    """Reconstruct path from BFS parent pointers."""
    if target not in parent:
        return []
    path: list[V] = []
    cur: V | None = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


def sample_graph() -> Graph[str]:
    return {
        "s": {"a", "b"},
        "a": {"s", "c", "d"},
        "b": {"s", "e", "f"},
        "c": {"a"},
        "d": {"a", "g"},
        "e": {"b", "g"},
        "f": {"b"},
        "g": {"d", "e"},
    }


if __name__ == "__main__":
    graph = sample_graph()
    dist, parent = bfs_distances(graph, "s")
    print("distances:", dict(sorted(dist.items())))
    print("path s->g:", reconstruct_path(parent, "g"))
