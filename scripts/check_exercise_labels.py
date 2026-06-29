#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "docs/exercises/core-exercises.md",
    ROOT / "docs/exercises/standard-exercises.md",
    ROOT / "docs/exercises/extended-exercises.md",
    ROOT / "docs/exercises/proof-drills.md",
    ROOT / "docs/exercises/asymptotic-drills.md",
    ROOT / "docs/exercises/pseudocode-recursion-drills.md",
    ROOT / "docs/exercises/integrated-readiness-test.md",
]
LABEL_RE = re.compile(r"\[(A|B|C|D|E)\]")


def main() -> int:
    errors: list[str] = []
    for path in FILES:
        text = path.read_text(encoding="utf-8")
        if "難易度ラベル" not in text:
            errors.append(f"missing legend: {path}")
        if not LABEL_RE.search(text):
            errors.append(f"missing labels: {path}")
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        return 1
    print("exercise labels OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
