#!/usr/bin/env python3
"""docs配下のMarkdownから許可されないASCII制御文字を検出する。"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ALLOWED_CONTROLS = {"\t", "\n", "\r"}


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    column: int
    codepoint: int

    def format(self) -> str:
        try:
            display_path = self.path.relative_to(ROOT)
        except ValueError:
            display_path = self.path
        return (
            f"{display_path}:{self.line}:{self.column}: "
            f"disallowed control character U+{self.codepoint:04X}"
        )


def is_disallowed_control(character: str) -> bool:
    codepoint = ord(character)
    return (
        (0x00 <= codepoint <= 0x1F and character not in ALLOWED_CONTROLS)
        or codepoint == 0x7F
    )


def find_disallowed_controls(text: str, path: Path = Path("<memory>")) -> list[Finding]:
    findings: list[Finding] = []
    line = 1
    column = 1
    for character in text:
        if is_disallowed_control(character):
            findings.append(Finding(path, line, column, ord(character)))
        if character == "\n":
            line += 1
            column = 1
        else:
            column += 1
    return findings


def scan_markdown_files(docs: Path = DOCS) -> tuple[list[Finding], list[str]]:
    findings: list[Finding] = []
    errors: list[str] = []
    if not docs.is_dir():
        return findings, [f"Markdown source directory is missing: {docs}"]
    for path in sorted(docs.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path}: invalid UTF-8: {exc}")
            continue
        findings.extend(find_disallowed_controls(text, path))
    return findings, errors


def main() -> int:
    findings, errors = scan_markdown_files()
    if findings or errors:
        for finding in findings:
            print(finding.format(), file=sys.stderr)
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("docs markdown control characters OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
