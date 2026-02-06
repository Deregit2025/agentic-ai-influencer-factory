
# Containerization Guide – Project Chimera

## Overview
This document explains the containerization setup for **Project Chimera**, an autonomous AI influencer prototype. The project uses Docker for reproducible development, testing, and deployment environments, ensuring that all agents and skills run consistently across machines.

---

## Dockerfile Structure

The Dockerfile follows a **multi-stage build** to reduce image size and isolate dependencies:

1. **Build Stage**
   - Uses the official Python 3.11 slim image.
   - Installs system dependencies: `git`, `ffmpeg`, `build-essential`.
   - Sets up Python environment using `uv` and locks dependency versions.
   - Performs a full sync to ensure all dev and runtime packages are installed.

2. **Runtime Stage**
   - Uses a minimal Python 3.11 slim image for the final runtime.
   - Copies only the necessary application code and dependencies.
   - Runs the container as a **non-root user** for security.
   - Exposes ports and sets entrypoints if required for agents or APIs.

---

## Environment Variables

The container recognizes the following environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `BASE_URL` | API base URL for agent interactions | `https://testcbrs.eaglelionsystems.com/v1.0/cbrs-api` |
| `LOG_LEVEL` | Logging verbosity (`DEBUG`, `INFO`, `WARN`, `ERROR`) | `INFO` |
| `MCP_SERVER` | Target MCP server URL for telemetry & analytics | Configured in `.vscode/mcp.json` |

> Additional variables can be added as needed. They should be documented in this file to ensure reproducibility.

---

## Build and Run Commands

### Build Image
```bash
docker build -t agentic_ai .
````

### Run Container (Interactive)

```bash
docker run -it --rm \
  -e BASE_URL="https://testcbrs.eaglelionsystems.com/v1.0/cbrs-api" \
  -v $(pwd):/app \
  agentic_ai
```

### Run Container in Detached Mode

```bash
docker run -d \
  -e BASE_URL="https://testcbrs.eaglelionsystems.com/v1.0/cbrs-api" \
  -v $(pwd):/app \
  --name agentic_ai_container \
  agentic_ai
```

---

## Reproducibility Considerations

* Use **locked dependency versions** in `pyproject.toml` to avoid inconsistencies.
* Multi-stage builds minimize unnecessary packages in the final image.
* Non-root runtime ensures safer execution and aligns with production best practices.
* Volumes allow local code changes to reflect in the container without rebuilding.

---

## CI/CD Integration

* Docker builds are integrated in the CI pipeline (GitHub Actions or other CI).
* Automated tests are run inside the container to ensure consistent environments.
* Optional security scans or linting can be added as Makefile targets to enforce best practices.

---

## References

* [Docker Official Docs](https://docs.docker.com/)
* [Python Docker Images](https://hub.docker.com/_/python)
* [uv Package – Python Environment Management](https://pypi.org/project/uv/)


