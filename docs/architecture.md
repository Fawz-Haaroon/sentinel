# Architecture (Overview)

- API: FastAPI (`app/`)
- Rules engine: deterministic URL scoring (`app/services/`)
- Config: YAML (`configs/`)
- CI: lint, type-check, tests (`.github/workflows/ci.yml`)
- Container: Dockerfile + compose (`docker/`)

