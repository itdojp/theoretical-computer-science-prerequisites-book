#!/usr/bin/env bash
set -euo pipefail

REMOTE_URL="${1:-git@github.com:itdojp/theoretical-computer-science-prerequisites-book.git}"

if [ ! -d .git ]; then
  git init
fi

git branch -M main
git add .
if git diff --cached --quiet; then
  echo "No changes to commit."
else
  git commit -m "Initial release: theoretical computer science prerequisites book"
fi

if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE_URL"
else
  git remote add origin "$REMOTE_URL"
fi

git push -u origin main
