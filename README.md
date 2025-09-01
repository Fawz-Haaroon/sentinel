# CyberSentinel

Lightweight multi-layered phishing & malware detection suite.

- URL/domain checks powered by regex/rules + scoring
- Obfuscation detection (shorteners, redirects)
- Static attachment checks (PDF/Office) – minimal, deterministic
- FastAPI service + simple dashboard skeleton
- CI, tests, and contributor tooling ready

Quickstart
- Requirements: Python 3.10+
- Install: pip install -r requirements.txt && pip install -r requirements-dev.txt
- Run dev: uvicorn app.main:app --reload
- Tests: pytest -q

Contributing
See CONTRIBUTING.md. Keep commits small and clear.

License
MIT (see LICENSE).

