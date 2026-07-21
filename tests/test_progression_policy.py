from __future__ import annotations

import pytest

from scripts.check_progression_policy import (
    check_policy,
    diagnosis_gate,
    has_markdown_link,
    integrated_gate,
)


def test_policy_documents_are_synchronized() -> None:
    assert check_policy() == []


@pytest.mark.parametrize(
    "link",
    [
        "](progression-policy.md)",
        "](progression-policy.md#共通の必須ゲート)",
        "](  progression-policy.md#共通の必須ゲート  )",
        "](<progression-policy.md#共通の必須ゲート>)",
        "](progression-policy.md \"正本\")",
    ],
)
def test_policy_link_accepts_anchor_and_whitespace(link: str) -> None:
    assert has_markdown_link(f"[共通ポリシー{link}", "progression-policy.md")


def test_policy_link_rejects_different_target() -> None:
    assert not has_markdown_link(
        "[別ページ](other-policy.md#共通の必須ゲート)", "progression-policy.md"
    )


@pytest.mark.parametrize(
    ("score", "expected"),
    [(67, False), (68, True), (69, True)],
)
def test_diagnosis_gate_boundaries(score: int, expected: bool) -> None:
    assert diagnosis_gate(score) is expected


@pytest.mark.parametrize(
    ("total_score", "proof_score", "expected"),
    [
        (42, 3, False),
        (43, 3, True),
        (44, 3, True),
        (43, 2, False),
        (43, 4, True),
    ],
)
def test_integrated_gate_boundaries(
    total_score: int, proof_score: int, expected: bool
) -> None:
    assert integrated_gate(total_score, proof_score) is expected


@pytest.mark.parametrize(
    ("function", "args"),
    [
        (diagnosis_gate, (-1,)),
        (diagnosis_gate, (81,)),
        (integrated_gate, (-1, 3)),
        (integrated_gate, (51, 3)),
        (integrated_gate, (43, -1)),
        (integrated_gate, (43, 7)),
    ],
)
def test_gate_rejects_out_of_range_scores(function, args: tuple[int, ...]) -> None:
    with pytest.raises(ValueError):
        function(*args)
