from __future__ import annotations


def hamming_distance(x: str, y: str) -> int:
    if len(x) != len(y):
        raise ValueError("Hamming distance requires equal lengths")
    return sum(a != b for a, b in zip(x, y))


def minimum_distance(codewords: set[str]) -> int:
    words = sorted(codewords)
    if len(words) < 2:
        raise ValueError("at least two codewords are required")
    lengths = {len(w) for w in words}
    if len(lengths) != 1:
        raise ValueError("all codewords must have equal length")
    best: int | None = None
    for i, x in enumerate(words):
        for y in words[i + 1 :]:
            d = hamming_distance(x, y)
            best = d if best is None else min(best, d)
    assert best is not None
    return best


def nearest_codewords(received: str, codewords: set[str]) -> tuple[int, list[str]]:
    distances = [(hamming_distance(received, w), w) for w in sorted(codewords)]
    best = min(d for d, _ in distances)
    return best, [w for d, w in distances if d == best]


if __name__ == "__main__":
    code = {"000", "111"}
    print("minimum distance:", minimum_distance(code))
    print("nearest to 001:", nearest_codewords("001", code))
