#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
CODE_FENCE_RE = re.compile(r"^\s*```")

IGNORE_SCHEMES = {"http", "https", "mailto", "tel", "sandbox"}


def iter_markdown_files() -> list[Path]:
    return sorted([*DOCS.rglob("*.md"), ROOT / "README.md", ROOT / "CHANGELOG.md", ROOT / "NOTICE.md"])


def strip_code_fences(text: str) -> str:
    out: list[str] = []
    in_code = False
    for line in text.splitlines():
        if CODE_FENCE_RE.match(line):
            in_code = not in_code
            out.append("")
            continue
        out.append("" if in_code else line)
    return "\n".join(out)


def normalize_link(raw: str) -> str | None:
    # Remove optional title: [x](path "title")
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        return None
    if " " in raw and not raw.startswith("<"):
        raw = raw.split()[0]
    raw = raw.strip("<>")
    parsed = urlparse(raw)
    if parsed.scheme in IGNORE_SCHEMES:
        return None
    if parsed.scheme:
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    return path


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    for md in iter_markdown_files():
        text = strip_code_fences(md.read_text(encoding="utf-8"))
        for match in LINK_RE.finditer(text):
            target = normalize_link(match.group(1))
            if target is None:
                continue
            candidate = (md.parent / target).resolve()
            if not str(candidate).startswith(str(ROOT.resolve())):
                errors.append(f"{md}: link escapes repository: {match.group(1)}")
                continue
            if not candidate.exists():
                errors.append(f"{md}: missing link target: {match.group(1)} -> {candidate}")
    return errors


def check_mkdocs_nav() -> list[str]:
    errors: list[str] = []
    yml = ROOT / "mkdocs.yml"
    if not yml.exists():
        return ["mkdocs.yml is missing"]
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover
        return [f"PyYAML unavailable: {exc}"]
    data = yaml.safe_load(yml.read_text(encoding="utf-8"))
    nav = data.get("nav", []) if isinstance(data, dict) else []

    def walk(node):
        if isinstance(node, str):
            yield node
        elif isinstance(node, list):
            for item in node:
                yield from walk(item)
        elif isinstance(node, dict):
            for value in node.values():
                yield from walk(value)

    for rel in walk(nav):
        if isinstance(rel, str) and rel.endswith(".md"):
            target = DOCS / rel
            if not target.exists():
                errors.append(f"mkdocs nav target missing: {rel}")
    return errors


def main() -> int:
    errors = check_markdown_links() + check_mkdocs_nav()
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("all markdown/mkdocs links OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
