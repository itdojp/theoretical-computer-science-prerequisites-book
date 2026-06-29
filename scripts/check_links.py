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
EXCLUDED_SITE_DIRS = {"audit", "release", "operations", "forms", "quality"}


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


def check_jekyll_navigation() -> list[str]:
    errors: list[str] = []
    nav_file = DOCS / "_data" / "navigation.yml"
    if not nav_file.exists():
        return ["docs/_data/navigation.yml is missing"]
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover
        return [f"PyYAML unavailable: {exc}"]

    data = yaml.safe_load(nav_file.read_text(encoding="utf-8")) or {}

    def walk(node):
        if isinstance(node, dict):
            if "path" in node:
                yield node["path"]
            for value in node.values():
                yield from walk(value)
        elif isinstance(node, list):
            for item in node:
                yield from walk(item)

    seen: set[str] = set()
    for raw in walk(data):
        if not isinstance(raw, str) or not raw.startswith("/"):
            errors.append(f"Jekyll navigation path must be absolute: {raw!r}")
            continue
        if raw in seen:
            errors.append(f"duplicate Jekyll navigation path: {raw}")
        seen.add(raw)
        rel = raw.strip("/")
        candidates = []
        if not rel:
            candidates.append(DOCS / "index.md")
        else:
            candidates.append(DOCS / f"{rel}.md")
            candidates.append(DOCS / rel / "index.md")
        if not any(p.exists() for p in candidates):
            errors.append(f"Jekyll navigation target missing: {raw}")
        first_part = rel.split("/", 1)[0] if rel else ""
        if first_part in EXCLUDED_SITE_DIRS:
            errors.append(f"repository-only directory must not be in published navigation: {raw}")
    return errors


def check_jekyll_config() -> list[str]:
    errors: list[str] = []
    cfg = DOCS / "_config.yml"
    if not cfg.exists():
        return ["docs/_config.yml is missing"]
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover
        return [f"PyYAML unavailable: {exc}"]
    data = yaml.safe_load(cfg.read_text(encoding="utf-8")) or {}
    excludes = data.get("exclude", []) if isinstance(data, dict) else []
    normalized = {str(item).strip("'").strip('"') for item in excludes}
    for path in EXCLUDED_SITE_DIRS:
        expected = f"{path}/"
        if expected not in normalized:
            errors.append(f"docs/_config.yml must exclude repository-only path: {expected}")
    return errors


def main() -> int:
    errors = check_markdown_links() + check_jekyll_navigation() + check_jekyll_config()
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("all markdown/Jekyll links OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
