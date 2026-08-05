.PHONY: format ruff-lint ty-lint sqlmesh-lint test install plan

install:
	uv sync --all-extras
	uv run -- prek install
	
ready: ruff-lint ty-lint sqlmesh-lint sqlmesh-test sqlmesh-external-refs
	uv run -- ruff format

# SQLMesh Commands
plan:
	uv run -- sqlmesh plan

# Formatting Commands
ruff-lint:
	uv run -- ruff check --fix

ty-lint:
	uv run -- ty check

sqlmesh-lint:
	uv run -- sqlmesh lint

sqlmesh-test:
	uv run -- sqlmesh test

sqlmesh-external-refs:
	rm -f external_models.yaml
	uv run -- sqlmesh create_external_models