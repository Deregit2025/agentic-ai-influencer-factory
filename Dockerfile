# ------------------------------
# Dockerfile for agentic_ai
# ------------------------------

# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ffmpeg \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install uv
RUN pip install "uv>=0.9.29"

# Sync dependencies using uv
RUN uv sync

# Optional: expose port if your project runs a service
# EXPOSE 8000

# Default command (can be overridden)
CMD ["python3"]
