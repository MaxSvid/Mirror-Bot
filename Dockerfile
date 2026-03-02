FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install uv from official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Install dependencies (separate layer for caching)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Copy source
COPY . .

CMD ["uv", "run", "python", "main.py"]
