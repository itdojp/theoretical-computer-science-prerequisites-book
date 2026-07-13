from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_link_checker() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts/check_links.py")], check=True, cwd=ROOT)


def test_exercise_label_checker() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts/check_exercise_labels.py")], check=True, cwd=ROOT)


def test_exercise_solution_mapping_checker() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts/check_exercise_solution_mapping.py")], check=True, cwd=ROOT)


def test_required_files_exist() -> None:
    required = [
        "docs/review/chapter-review-problems.md",
        "docs/review/chapter-review-solutions.md",
        "docs/assessment/grading-forms.md",
        "docs/exercises/labeled-exercise-index.md",
        "docs/quality/ci-and-quality-control.md",
        "docs/audit/v1-release-candidate-audit.md",
        "docs/audit/style-and-terminology.md",
        "docs/audit/exercise-solution-mapping.md",
        "docs/audit/scope-boundary-audit.md",
        "docs/audit/license-finalization.md",
        "docs/audit/release-checklist-v1.md",
        "LICENSE",
        "LICENSE-DOCS.md",
        "LICENSE-CODE.md",
        "CITATION.cff",
        "VERSION",
        "RELEASE.md",
        "docs/release/release-metadata.md",
        "docs/release/github-release-notes-v1.0.md",
        "docs/release/publication-guide.md",
        "docs/release/final-release-audit.md",
        "docs/operations/instructor-guide.md",
        "docs/operations/cohort-operations-guide.md",
        "docs/operations/reading-group-facilitation.md",
        "docs/operations/assignment-submission-format.md",
        "docs/operations/learner-progress-template.md",
        "docs/operations/release-process.md",
        "docs/operations/contribution-guide.md",
        "docs/operations/license-and-citation-policy.md",
        "docs/operations/maintenance-playbook.md",
        "docs/forms/assignment-submission.md",
        "docs/forms/review-meeting-notes.md",
        "docs/forms/release-checklist.md",
        "docs/forms/learner-progress.csv",
        "docs/forms/cohort-dashboard.csv",
        "CONTRIBUTING.md",
        "LICENSE-POLICY.md",
        ".github/ISSUE_TEMPLATE/content-fix.md",
        ".github/ISSUE_TEMPLATE/exercise-fix.md",
        ".github/ISSUE_TEMPLATE/operations.md",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/workflows/ci.yml",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel


def test_concept_map_reader_route_is_published() -> None:
    route = "/reference/concept-map/"
    source = ROOT / "docs" / f"{route.strip('/')}.md"
    assert source.exists()
    source_text = source.read_text(encoding="utf-8")
    assert source_text.startswith("# 概念依存マップ\n")
    for related_page in (
        "concept-index.md",
        "../learning-path.md",
        "../navigation/chapter-link-map.md",
        "../navigation/main-textbook-reverse-index.md",
        "../appendix/mapping-to-main-textbook.md",
    ):
        assert related_page in source_text

    navigation = yaml.safe_load(
        (ROOT / "docs/_data/navigation.yml").read_text(encoding="utf-8")
    )
    assert {"title": "概念依存マップ", "path": route} in navigation["resources"]

    config = json.loads((ROOT / "book-config.json").read_text(encoding="utf-8"))
    assert config["ux"]["modules"]["conceptMap"] is True

    search_data = json.loads(
        (ROOT / "docs/assets/search-data.json").read_text(encoding="utf-8")
    )
    assert {
        "title": "概念依存マップ",
        "url": "/theoretical-computer-science-prerequisites-book/reference/concept-map/",
        "source_path": "docs/reference/concept-map.md",
    }.items() <= next(
        item
        for item in search_data["items"]
        if item.get("source_path") == "docs/reference/concept-map.md"
    ).items()

    for entrypoint in ("docs/index.md", "docs/learning-path.md"):
        text = (ROOT / entrypoint).read_text(encoding="utf-8")
        assert "[概念依存マップ](reference/concept-map.md)" in text

    navigation_guide = (ROOT / "docs/navigation/navigation-guide.md").read_text(
        encoding="utf-8"
    )
    assert "[概念依存マップ](../reference/concept-map.md)" in navigation_guide
    assert "[章間リンクマップ](chapter-link-map.md)" in navigation_guide
