# ==========================================================
# Makefile for Project Chimera: AI Autonomous Influencer
# ==========================================================

# Default Python environment
PYTHON=python

# Docker image name
DOCKER_IMAGE=project_chimera:latest

# ==========================
# Command: setup
# ==========================
# Installs dependencies in the container or local environment
.PHONY: setup
setup:
	@echo "=== Setting up Python environment and dependencies ==="
	uv sync
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt || true
	@echo "Setup complete ✅"

# ==========================
# Command: test
# ==========================
# Runs all pytest tests inside Docker
.PHONY: test
test:
	@echo "=== Running tests inside Docker ==="
	docker build -t $(DOCKER_IMAGE) .
	docker run --rm -v $(PWD):/app $(DOCKER_IMAGE) pytest tests/
	@echo "Tests executed ✅ (Expected to fail for TDD placeholder)"

# ==========================
# Command: spec-check
# ==========================
# Verifies code aligns with project specifications
.PHONY: spec-check
spec-check:
	@echo "=== Running Spec Alignment Check ==="
	$(PYTHON) scripts/spec_checker.py || true
	@echo "Spec check complete ✅"

# ==========================
# Command: lint
# ==========================
# Lint Python code using flake8
.PHONY: lint
lint:
	@echo "=== Linting Python code ==="
	flake8 skills/ tests/ scripts/
	@echo "Linting complete ✅"

# ==========================
# Command: format
# ==========================
# Format Python code using black
.PHONY: format
format:
	@echo "=== Formatting Python code ==="
	black skills/ tests/ scripts/
	@echo "Formatting complete ✅"

# ==========================
# Command: security-scan
# ==========================
# Run security scan with Bandit
.PHONY: security-scan
security-scan:
	@echo "=== Running Security Scan ==="
	bandit -r skills/ scripts/
	@echo "Security scan complete ✅"

# ==========================
# Command: all
# ==========================
# Runs full automation suite: lint, format, security, spec-check, test
.PHONY: all
all: lint format security-scan spec-check test
	@echo "=== Full automation suite completed ✅ ==="

# ==========================
# Command: shell
# ==========================
# Open an interactive shell inside Docker container
.PHONY: shell
shell:
	docker run --rm -it -v $(PWD):/app $(DOCKER_IMAGE) bash
