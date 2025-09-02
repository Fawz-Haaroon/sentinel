PHONY: sentinel

ARGS := $(filter-out $@,$(MAKECMDGOALS))

# Python virtual environment
venv:
	python3 -m venv venv

# Install dependencies
install:
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt
	./venv/bin/pip install -e .

# Run development server
dev:
	cd app && ../venv/bin/uvicorn server:app --reload

# Run production server
run:
	cd app && ../venv/bin/uvicorn server:app --host 0.0.0.0 --port 8000

sentinel:
	./venv/bin/$(ARGS)

# Prevent make from treating 'detect', URLs, etc. as targets
%:
	@:

# Run tests
test:
	./venv/bin/pytest

# Clean cache and build files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache .mypy_cache build dist

# Show help
help:
	@echo "Available commands:"
	@echo "  venv     - Create virtual environment"
	@echo "  install  - Install dependencies"
	@echo "  dev      - Run app in development mode"
	@echo "  run      - Run app in production mode"
	@echo "  test     - Run pytest"
	@echo "  clean    - Remove cache/build files"
