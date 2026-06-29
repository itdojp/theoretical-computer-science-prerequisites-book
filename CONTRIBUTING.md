# Contributing

本教材への修正・追加は、前提補強という目的に合う範囲で行います。

詳細は [コントリビューションガイド](docs/operations/contribution-guide.md) を参照してください。

リリース前には、最低限、次を実行します。

```bash
python scripts/check_links.py
python scripts/check_exercise_labels.py
python examples/python/tests.py
python -m pytest
```
