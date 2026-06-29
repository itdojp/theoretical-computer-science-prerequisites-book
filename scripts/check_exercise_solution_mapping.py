#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class ExerciseSet:
    name: str
    problem_file: Path
    solution_file: Path
    problem_pattern: re.Pattern[str]
    solution_pattern: re.Pattern[str]
    expected_count: int
    prefix: str | None = None
    solution_prefix_to_problem: str | None = None


def normalize(ids: list[str], prefix: str | None = None) -> list[str]:
    out: list[str] = []
    for x in ids:
        if prefix is None:
            out.append(str(int(x)))
        elif x.startswith(prefix):
            out.append(f"{prefix}{int(x[len(prefix):])}")
        else:
            out.append(f"{prefix}{int(x)}")
    return out


SETS = [
    ExerciseSet(
        name="Core 演習",
        problem_file=ROOT / "docs/exercises/core-exercises.md",
        solution_file=ROOT / "docs/exercises/solutions.md",
        problem_pattern=re.compile(r"^\s*(\d+)\.\s+\*\*\[", re.MULTILINE),
        solution_pattern=re.compile(r"^\*\*(\d+)\.", re.MULTILINE),
        expected_count=70,
    ),
    ExerciseSet(
        name="Standard 演習",
        problem_file=ROOT / "docs/exercises/standard-exercises.md",
        solution_file=ROOT / "docs/exercises/standard-solutions.md",
        problem_pattern=re.compile(r"^###\s+(S\d+)\b", re.MULTILINE),
        solution_pattern=re.compile(r"^###\s+(S\d+)\b", re.MULTILINE),
        expected_count=60,
        prefix="S",
    ),
    ExerciseSet(
        name="Extended 演習",
        problem_file=ROOT / "docs/exercises/extended-exercises.md",
        solution_file=ROOT / "docs/exercises/extended-solutions.md",
        problem_pattern=re.compile(r"^\*\*(E\d+)\.\*\*", re.MULTILINE),
        solution_pattern=re.compile(r"^\*\*(E\d+)\.\*\*", re.MULTILINE),
        expected_count=80,
        prefix="E",
    ),
    ExerciseSet(
        name="統合到達確認テスト",
        problem_file=ROOT / "docs/exercises/integrated-readiness-test.md",
        solution_file=ROOT / "docs/exercises/integrated-readiness-solutions.md",
        problem_pattern=re.compile(r"^\*\*(Q\d+)\.\*\*", re.MULTILINE),
        solution_pattern=re.compile(r"^\*\*A(\d+)\.\*\*", re.MULTILINE),
        expected_count=50,
        prefix="Q",
    ),
]


def extract_ids(spec: ExerciseSet) -> tuple[list[str], list[str]]:
    problems_raw = spec.problem_pattern.findall(spec.problem_file.read_text(encoding="utf-8"))
    solutions_raw = spec.solution_pattern.findall(spec.solution_file.read_text(encoding="utf-8"))
    problems = normalize(problems_raw, spec.prefix)
    solutions = normalize(solutions_raw, spec.prefix)
    return problems, solutions


def contiguous_ids(ids: list[str], expected_count: int, prefix: str | None) -> list[str]:
    if prefix is None:
        return [str(i) for i in range(1, expected_count + 1)]
    return [f"{prefix}{i}" for i in range(1, expected_count + 1)]


def check_set(spec: ExerciseSet) -> list[str]:
    errors: list[str] = []
    problems, solutions = extract_ids(spec)
    expected = contiguous_ids(problems, spec.expected_count, spec.prefix)

    if problems != expected:
        errors.append(
            f"{spec.name}: problem ids are not contiguous {expected[0]}..{expected[-1]} "
            f"or count mismatch: found {len(problems)}"
        )
    if solutions != expected:
        errors.append(
            f"{spec.name}: solution ids are not contiguous {expected[0]}..{expected[-1]} "
            f"or count mismatch: found {len(solutions)}"
        )

    missing = sorted(set(problems) - set(solutions), key=lambda x: int(re.sub(r"\D", "", x)))
    extra = sorted(set(solutions) - set(problems), key=lambda x: int(re.sub(r"\D", "", x)))
    if missing:
        errors.append(f"{spec.name}: missing solutions for {', '.join(missing)}")
    if extra:
        errors.append(f"{spec.name}: solution ids without problems {', '.join(extra)}")
    return errors


def main() -> int:
    errors: list[str] = []
    for spec in SETS:
        errors.extend(check_set(spec))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("exercise/solution mappings OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
