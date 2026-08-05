# sqlmesh-test-project

Basic Setup for Open Source Deployment. Points at BigQuery and uses GCP Cloud SQL Postgres instance for the backend.

## GCP Setup

1. Have BigQuery Enabled
2. Create a Cloud SQL Postgres Instance
3. Create a database for the state backend -- Get the connection string
4. Create a SQLMesh User for the database -- Username / Password
5. Create a GCP service account and download a json keyfile
6. Rename it to `keyfile.json` and place it in the root of the repo

## Repo Setup

1. Download `uv`
2. Run `make install`
3. Fill out `.env` file -- reference `.env.example` file

## Current Configuration

See the `config.py` file. It MUST be named `config.py` and have a `config` object in it.

### Production Gateway
 - Connection: BigQuery
 - State Connection: Cloud SQL (Postgres)
 - Test Connection: DuckDB
 
### Linter
 - Enabled
 - Rules:
    - Ambiguous Invalid Columns
    - Invalid Select Star Expansion
    - No Ambiguous Projections
    - No Missing Audits
    - No Missing Unit Tests