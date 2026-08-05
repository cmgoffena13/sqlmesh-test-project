# CI/CD Walkthrough

For use if you don't use the Github CI/CD Bot.

## Build Stage - Create Environment
```
uv lock --check
uv sync --frozen --no-dev
uv cache prune --ci
```

## MR Opened - Validate Plan
Option 1 -- Run last 30 days of data with a plan for validation
```bash
uv sync --frozen --no-dev
uv run --no-sync -- sqlmesh plan dev_MR_{Merge Request ID} --no-prompts --auto-apply -s "$(date -d '30 days ago' '+%Y-%m-%d')"
```
Option 2 -- Validate the plan without running any data through
```bash
uv sync --frozen --no-dev
uv run --no-sync -- sqlmesh plan dev_MR_{Merge Request ID} --no-prompts --auto-apply --skip-backfill
```

## Merge into Main - Deploy to Prod

Depends on how much memory your runner has, probably at least 4GB. Otherwise you have to trigger an outside job and wait/poll for completion

```bash
uv sync --frozen --no-dev
uv run --no-sync -- sqlmesh plan prod --no-prompts --auto-apply
```

