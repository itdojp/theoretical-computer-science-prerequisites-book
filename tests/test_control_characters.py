from __future__ import annotations

from pathlib import Path

import pytest

from scripts.check_control_characters import (
    find_disallowed_controls,
    scan_markdown_files,
)

ROOT = Path(__file__).resolve().parents[1]


def test_docs_have_no_disallowed_control_characters() -> None:
    findings, errors = scan_markdown_files()
    assert errors == []
    assert findings == []


def test_allowed_whitespace_is_not_reported() -> None:
    assert find_disallowed_controls("見出し\t本文\r\n次の行\n") == []


@pytest.mark.parametrize("codepoint", [0x00, 0x08, 0x0B, 0x0C, 0x1F, 0x7F])
def test_disallowed_control_character_is_reported(codepoint: int) -> None:
    findings = find_disallowed_controls(f"日本語{chr(codepoint)}marker")
    assert len(findings) == 1
    assert findings[0].codepoint == codepoint
    assert findings[0].line == 1
    assert findings[0].column == 4


def test_markdown_scan_finds_negative_fixture(tmp_path: Path) -> None:
    fixture = tmp_path / "nested" / "broken.md"
    fixture.parent.mkdir()
    fixture.write_text("正常\n破損\x08marker\n", encoding="utf-8")
    findings, errors = scan_markdown_files(tmp_path)
    assert errors == []
    assert [(item.path, item.line, item.column, item.codepoint) for item in findings] == [
        (fixture, 2, 3, 0x08)
    ]


def test_counting_chapter_contains_literal_binomial_notation() -> None:
    text = (ROOT / "docs/part-2-standard/07-counting.md").read_text(encoding="utf-8")
    assert "\\binom{n}{k}" in text
