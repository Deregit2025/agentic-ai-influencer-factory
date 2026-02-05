# ==========================================================
# Dockerfile for Project Chimera: Autonomous AI Influencer
# ==========================================================

# Base image with Python 3.11
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PROJECT_DIR=/app

# Set working directory
WORKDIR $PROJECT_DIR

# Copy project files
COPY . .

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies (assuming pyproject.toml exists)
RUN pip install --upgrade pip \
    && pip install "uv" \
    && uv sync

# Optional: install pytest inside container for TDD
RUN pip install pytest

# Expose ports if agent uses any API services
EXPOSE 8000

# Default command: keep container alive and ready for commands
CMD ["sleep", "infinity"]
