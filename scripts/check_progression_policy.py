#!/usr/bin/env python3
"""本体教科書への進行判定ポリシーと参照ページの同期を検査する。"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DIAGNOSIS_MIN = 68
DIAGNOSIS_MAX = 80
INTEGRATED_MIN = 43
INTEGRATED_MAX = 50
PROOF_MIN = 3
PROOF_MAX = 6

POLICY = ROOT / "docs/assessment/progression-policy.md"

REQUIRED_REFERENCES = {
    "docs/diagnosis.md": "assessment/progression-policy.md",
    "docs/learning-path.md": "assessment/progression-policy.md",
    "docs/exercises/integrated-readiness-test.md": "../assessment/progression-policy.md",
    "docs/assessment/attainment-criteria.md": "progression-policy.md",
    "docs/assessment/scoring-rubric.md": "progression-policy.md",
    "docs/assessment/grading-forms.md": "progression-policy.md",
    "docs/assessment/learning-checklists.md": "progression-policy.md",
    "docs/assessment/main-textbook-readiness.md": "progression-policy.md",
    "docs/assessment/recovery-routes.md": "progression-policy.md",
    "docs/operations/instructor-guide.md": "../assessment/progression-policy.md",
}

REQUIRED_POLICY_SNIPPETS = (
    "progression-policy:diagnosis=68/80",
    "progression-policy:integrated=43/50",
    "progression-policy:proof=3/6",
    "67/80: 未達",
    "68/80: 達成",
    "69/80: 達成",
    "42/50: 未達",
    "43/50: 達成",
    "44/50: 達成",
    "2/6: 未達",
    "3/6: 達成",
    "4/6: 達成",
    "対象章別 readiness の「不可」条件を総合得点で上書きしてはいけません",
)

REQUIRED_PAGE_SNIPPETS = {
    "docs/diagnosis.md": ("| 68〜80 | 診断ゲート達成 |",),
    "docs/exercises/integrated-readiness-test.md": (
        "合計43/50以上",
        "証明問題 Q7〜Q10・Q23・Q49 の3/6以上",
    ),
    "docs/assessment/learning-checklists.md": (
        "前提診断で68/80以上",
        "統合到達確認テストで43/50以上",
        "証明問題で3/6以上",
    ),
    "docs/operations/instructor-guide.md": (
        "80問中68問以上",
        "50問中43問以上、かつ証明問題6問中3問以上",
    ),
}

FORBIDDEN_PATTERNS = {
    "前提診断60問基準": re.compile(r"前提診断[^\n]{0,40}(?:60問以上|60/80以上)"),
    "前提診断64問基準": re.compile(r"前提診断[^\n]{0,40}(?:64問以上|64/80以上)"),
    "統合test70%進行基準": re.compile(
        r"統合到達確認テストで\s*70(?:%|％)以上(?:正答)?"
    ),
    "統合test35問進行基準": re.compile(
        r"統合到達確認テスト[^\n]{0,50}(?:35問以上|35/50以上)"
    ),
    "旧43点単独進行表現": re.compile(r"43点以上で本体教科書へ進行可"),
}


def diagnosis_gate(score: int) -> bool:
    if not 0 <= score <= DIAGNOSIS_MAX:
        raise ValueError(f"diagnosis score out of range: {score}")
    return score >= DIAGNOSIS_MIN


def integrated_gate(total_score: int, proof_score: int) -> bool:
    if not 0 <= total_score <= INTEGRATED_MAX:
        raise ValueError(f"integrated score out of range: {total_score}")
    if not 0 <= proof_score <= PROOF_MAX:
        raise ValueError(f"proof score out of range: {proof_score}")
    return total_score >= INTEGRATED_MIN and proof_score >= PROOF_MIN


def has_markdown_link(text: str, target: str) -> bool:
    """指定先へのMarkdownリンクを、任意の空白・見出しアンカー込みで検出する。"""
    pattern = re.compile(
        rf"\]\(\s*<?{re.escape(target)}(?:#[^)\s>]*)?>?"
        r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
    )
    return pattern.search(text) is not None


def check_policy() -> list[str]:
    errors: list[str] = []
    if not POLICY.exists():
        return [f"missing canonical policy: {POLICY.relative_to(ROOT)}"]

    policy_text = POLICY.read_text(encoding="utf-8")
    for snippet in REQUIRED_POLICY_SNIPPETS:
        if snippet not in policy_text:
            errors.append(f"canonical policy missing required text: {snippet!r}")

    for rel, target in REQUIRED_REFERENCES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing policy consumer: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if not has_markdown_link(text, target):
            errors.append(f"{rel} does not link to canonical policy via {target}")

    for rel, snippets in REQUIRED_PAGE_SNIPPETS.items():
        path = ROOT / rel
        if not path.exists():
            if rel not in REQUIRED_REFERENCES:
                errors.append(f"missing synchronized policy page: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for snippet in snippets:
            if snippet not in text:
                errors.append(f"{rel} missing synchronized criterion: {snippet!r}")

    scan_paths = sorted((ROOT / "docs").rglob("*.md"))
    search_data = ROOT / "docs/assets/search-data.json"
    if search_data.exists():
        scan_paths.append(search_data)
    else:
        errors.append("missing policy search data: docs/assets/search-data.json")
    for path in scan_paths:
        text = path.read_text(encoding="utf-8")
        for label, pattern in FORBIDDEN_PATTERNS.items():
            match = pattern.search(text)
            if match:
                rel = path.relative_to(ROOT)
                errors.append(f"{rel}: {label}: {match.group(0)!r}")

    return errors


def main() -> int:
    errors = check_policy()
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("progression policy is synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
