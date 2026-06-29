from __future__ import annotations

import subprocess
import sys
from pathlib import Path

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
