# sqlmesh-test-project

Basic Setup for Open Source Deployment

## Setup

1. Run `make install`

## Current Configuration

### Production Gateway
 - Connection: BigQuery
 - State Connection: DuckDB (Recommended: Postgres)

### Linter
 - Enabled
 - Rules:
    - Ambiguous Invalid Columns
    - Invalid Select Star Expansion
    - No Ambiguous Projections
    - No Missing Audits
    - No Missing Unit Tests