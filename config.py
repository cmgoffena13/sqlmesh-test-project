# Documentation: https://sqlmesh.readthedocs.io/en/latest/_readthedocs/html/sqlmesh/core/config.html

from sqlmesh.core.config import (
    BigQueryConnectionConfig,
    BuiltInSchedulerConfig,
    Config,
    DuckDBConnectionConfig,
    GatewayConfig,
    LinterConfig,
    ModelDefaultsConfig,
)
from sqlmesh.core.config.connection import BigQueryConnectionMethod

config = Config(
    gateways={
        "production": GatewayConfig(
            connection=BigQueryConnectionConfig(
                project="crypto-topic-479022-e7",
                keyfile="keyfile.json",
                method=BigQueryConnectionMethod.OAUTH,
            ),
            state_connection=DuckDBConnectionConfig(
                database="state.db",
            ),
            scheduler=BuiltInSchedulerConfig(),
        )
    },
    default_gateway="production",
    model_defaults=ModelDefaultsConfig(
        dialect="bigquery",
        start="2025-01-01",
        cron="@daily",
    ),
    linter=LinterConfig(
        enabled=True,
        rules={
            "ambiguousorinvalidcolumn",
            "invalidselectstarexpansion",
            "noambiguousprojections",
            "nomissingaudits",
            "nomissingunittest",
        },
    ),
)
