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
from sqlmesh.core.config.connection import BigQueryConnectionMethod, GCPPostgresConnectionConfig
from sqlmesh.core.notification_target import NotificationEvent, SlackWebhookNotificationTarget

from settings import settings

config = Config(
    gateways={
        "production": GatewayConfig(
            connection=BigQueryConnectionConfig(
                project=settings.GOOGLE_PROJECT,
                keyfile="keyfile.json",
                method=BigQueryConnectionMethod.OAUTH,
                concurrent_tasks=5,
            ),
            state_connection=GCPPostgresConnectionConfig(
                instance_connection_string=settings.CLOUD_SQL_INSTANCE_CONNECTION_STRING,
                db="test",
                user=settings.CLOUD_SQL_USER,
                ip_type="public",
                keyfile="db_keyfile.json",
                enable_iam_auth=True,
                concurrent_tasks=5,
                timeout=30,
            ),
            test_connection=DuckDBConnectionConfig(
                database="test.db",
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
    notification_targets=[
        SlackWebhookNotificationTarget(
            url=settings.SLACK_WEBHOOK_URL,
            notify_on=frozenset(
                [
                    NotificationEvent.APPLY_FAILURE,
                    NotificationEvent.RUN_FAILURE,
                    NotificationEvent.AUDIT_FAILURE,
                    NotificationEvent.MIGRATION_FAILURE,
                ]
            ),
        )
    ],
    pinned_environments={"dev_cort"},
    log_limit=10,
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
