#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]

EXCLUDE_DIRS = {
    ".git",
    ".pytest_cache",
    "__pycache__",
    "site",
}
EXCLUDE_SUFFIXES = {".pyc", ".pyo"}


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        if path.is_file() and path.suffix not in EXCLUDE_SUFFIXES:
            yield path, rel


def make_zip(version: str, suffix: str, output_dir: Path) -> Path:
    dirname = f"theoretical-computer-science-prerequisites-book-{version}-{suffix}"
    zip_path = output_dir / f"{dirname}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with ZipFile(zip_path, "w", ZIP_DEFLATED) as zf:
        for path, rel in iter_files(ROOT):
            zf.write(path, Path(dirname) / rel)
    return zip_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Create release ZIP archive.")
    parser.add_argument("--version", required=True, help="Version string, e.g. v1.0-rc")
    parser.add_argument("--suffix", default="operations", help="Release suffix")
    parser.add_argument("--output-dir", default=str(ROOT.parent), help="Output directory")
    args = parser.parse_args()

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = make_zip(args.version, args.suffix, output_dir)
    print(zip_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
