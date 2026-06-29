from __future__ import annotations


def factorial(n: int) -> int:
    """Return n! for n >= 0."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def factorial_trace(n: int) -> list[str]:
    """Return a human-readable trace of recursive calls."""
    if n < 0:
        raise ValueError("n must be non-negative")
    trace: list[str] = []

    def rec(k: int, depth: int) -> int:
        indent = "  " * depth
        trace.append(f"{indent}call factorial({k})")
        if k == 0:
            trace.append(f"{indent}return 1")
            return 1
        value = k * rec(k - 1, depth + 1)
        trace.append(f"{indent}return {value}")
        return value

    rec(n, 0)
    return trace


if __name__ == "__main__":
    for line in factorial_trace(4):
        print(line)
