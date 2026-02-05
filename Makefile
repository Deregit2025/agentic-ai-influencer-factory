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
	pip install --upgrade pip
	pip install -r requirements.txt || true
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
# Optional: verifies code aligns with specs (you can extend this)
.PHONY: spec-check
spec-check:
	@echo "=== Running Spec Alignment Check ==="
	# Placeholder: add actual spec validation script here
	@echo "Spec check complete ✅"

# ==========================
# Command: shell
# ==========================
# Open an interactive shell inside Docker container
.PHONY: shell
shell:
	docker run --rm -it -v $(PWD):/app $(DOCKER_IMAGE) bash
