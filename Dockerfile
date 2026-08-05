ARG UV_VERSION=0.9.15
ARG PYTHON_VERSION=3.12
ARG UV_IMAGE_TYPE=trixie-slim
ARG IMAGE_TYPE=slim-trixie

FROM ghcr.io/astral-sh/uv:${UV_VERSION}-python${PYTHON_VERSION}-${UV_IMAGE_TYPE} AS builder

ENV UV_LINK_MODE=copy UV_COMPILE_BYTECODE=1 UV_PYTHON_DOWNLOADS=never

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-install-project

COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

FROM python:${PYTHON_VERSION}-${IMAGE_TYPE} AS runtime

RUN groupadd -r appgroup &&  \
    useradd -r -g appgroup -d /app appuser

ENV PATH="/app/.venv/bin:$PATH" PYTHONUNBUFFERED=1 HOME=/app SQLMESH_HOME=/app/.sqlmesh

WORKDIR /app

COPY --from=builder --chown=appuser:appgroup /app /app

# NOTE: Fix SQLMesh ownership issues.
RUN mkdir -p /app/.cache /app/.sqlmesh /app/tmp/sqlmesh-exports && chown -R appuser:appgroup /app

USER appuser
ENTRYPOINT ["python", "-m"]