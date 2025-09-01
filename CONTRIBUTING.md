# Contributing

- Use short, clear commits (present tense). Example: `feat: url scoring stub`
- Branches: `type/short-topic` (feat, fix, chore, docs, test, ci)
- Lint/format/type-check before pushing: `ruff`, `black`, `mypy`
- Tests: `pytest -q`
- PRs: small, focused; include context and screenshots if UI

## Dev setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
pre-commit install
uvicorn app.main:app --reload
```

## Commit style
- Keep subjects under ~50 chars.
- Body optional; only when needed.

