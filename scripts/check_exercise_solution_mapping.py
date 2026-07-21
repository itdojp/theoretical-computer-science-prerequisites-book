#!/usr/bin/env python3
from __future__ import annotations

import json
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
    require_explicit_anchors: bool = False


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
        name="Standard グラフ演習",
        problem_file=ROOT / "docs/exercises/standard-exercises.md",
        solution_file=ROOT / "docs/exercises/standard-solutions.md",
        problem_pattern=re.compile(r"^###\s+(G\d+)\b", re.MULTILINE),
        solution_pattern=re.compile(r"^###\s+(G\d+)\b", re.MULTILINE),
        expected_count=12,
        prefix="G",
        require_explicit_anchors=True,
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
    if spec.require_explicit_anchors:
        for path, ids, kind in (
            (spec.problem_file, problems, "problem"),
            (spec.solution_file, solutions, "solution"),
        ):
            text = path.read_text(encoding="utf-8")
            for exercise_id in ids:
                anchor = exercise_id.lower()
                pattern = re.compile(
                    rf"^###\s+{re.escape(exercise_id)}\b[^\n]*\n"
                    rf"\{{:\s*#{re.escape(anchor)}\s*\}}$",
                    re.MULTILINE,
                )
                if not pattern.search(text):
                    errors.append(
                        f"{spec.name}: {kind} {exercise_id} is missing explicit anchor #{anchor}"
                    )
    return errors


def check_review_grading_guide() -> list[str]:
    """章別レビューの採点観点を完全解答と誤認させない公開契約を検査する。"""
    errors: list[str] = []
    paths = {
        "problems": ROOT / "docs/review/chapter-review-problems.md",
        "guide": ROOT / "docs/review/chapter-review-solutions.md",
        "index": ROOT / "docs/index.md",
        "learning_path": ROOT / "docs/learning-path.md",
        "navigation": ROOT / "docs/_data/navigation.yml",
        "search": ROOT / "docs/assets/search-data.json",
    }
    missing = [str(path.relative_to(ROOT)) for path in paths.values() if not path.exists()]
    if missing:
        return [f"review grading guide contract: missing {path}" for path in missing]

    problems = paths["problems"].read_text(encoding="utf-8")
    guide = paths["guide"].read_text(encoding="utf-8")
    index = paths["index"].read_text(encoding="utf-8")
    learning_path = paths["learning_path"].read_text(encoding="utf-8")
    navigation = paths["navigation"].read_text(encoding="utf-8")

    required = {
        "docs/review/chapter-review-problems.md": (
            problems,
            "[章別レビュー問題 採点観点](chapter-review-solutions.md)",
            "完全解答ではありません",
        ),
        "docs/review/chapter-review-solutions.md": (
            guide,
            "# 章別レビュー問題 採点観点",
            "完全な答案例ではありません",
            "問題1〜5に同じ順序で対応します",
        ),
        "docs/index.md": (
            index,
            "[章別レビュー問題 採点観点（完全解答ではありません）](review/chapter-review-solutions.md)",
        ),
        "docs/learning-path.md": (
            learning_path,
            "[章別レビュー問題 採点観点](review/chapter-review-solutions.md)",
        ),
        "docs/_data/navigation.yml": (
            navigation,
            "title: 章別レビュー問題 採点観点",
            "path: /review/chapter-review-solutions/",
        ),
    }
    for rel, (text, *snippets) in required.items():
        for snippet in snippets:
            if snippet not in text:
                errors.append(f"{rel}: missing review grading guide text: {snippet!r}")

    forbidden = re.compile(r"章別レビュー問題\s+解答(?:・採点観点)?")
    for rel, text in (
        ("docs/review/chapter-review-problems.md", problems),
        ("docs/review/chapter-review-solutions.md", guide),
        ("docs/index.md", index),
        ("docs/learning-path.md", learning_path),
        ("docs/_data/navigation.yml", navigation),
    ):
        match = forbidden.search(text)
        if match:
            errors.append(f"{rel}: reader-facing complete-solution label remains: {match.group(0)!r}")

    try:
        search_data = json.loads(paths["search"].read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        errors.append(f"docs/assets/search-data.json: cannot inspect review guide: {exc}")
    else:
        items = search_data.get("items")
        if not isinstance(items, list):
            errors.append("docs/assets/search-data.json: items must be a list")
            items = []
        matches = [
            item
            for item in items
            if isinstance(item, dict)
            and item.get("source_path") == "docs/review/chapter-review-solutions.md"
        ]
        if len(matches) != 1:
            errors.append(
                "docs/assets/search-data.json: review grading guide must have exactly one item"
            )
        else:
            item = matches[0]
            if item.get("title") != "章別レビュー問題 採点観点":
                errors.append("docs/assets/search-data.json: review guide title is not synchronized")
            expected_url = (
                "/theoretical-computer-science-prerequisites-book/"
                "review/chapter-review-solutions/"
            )
            if item.get("url") != expected_url:
                errors.append(
                    "docs/assets/search-data.json: review guide public URL is not preserved"
                )
            excerpt = item.get("excerpt", "")
            if not isinstance(excerpt, str) or "完全な答案例ではありません" not in excerpt:
                errors.append(
                    "docs/assets/search-data.json: review guide excerpt must disclose that it is not a complete solution"
                )
            elif forbidden.search(excerpt):
                errors.append(
                    "docs/assets/search-data.json: review guide excerpt retains a complete-solution label"
                )

    return errors


def main() -> int:
    errors: list[str] = []
    for spec in SETS:
        errors.extend(check_set(spec))
    errors.extend(check_review_grading_guide())
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("exercise/solution mappings OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
