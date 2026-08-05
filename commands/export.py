from datetime import datetime, timezone
from pathlib import Path

from sqlmesh.core.context import Context
from sqlmesh.core.state_sync.export_import import export_state

from config import config


def export_state_to_local(context: Context, local_path: Path) -> None:
    context.state_sync.get_versions(validate=True)
    local_path.parent.mkdir(parents=True, exist_ok=True)

    export_state(
        state_sync=context.state_sync,
        output_file=local_path,
        local_snapshots=None,
        environment_names=None,
        console=context.console,
    )


if __name__ == "__main__":
    context = Context(config=config)

    export_datetime = datetime.now(timezone.utc)
    export_date = export_datetime.date().isoformat()
    timestamp = export_datetime.strftime("%Y%m%dT%H%M%SZ")

    local_path = Path() / export_date / f"sqlmesh-state-{timestamp}.json"

    export_state_to_local(context, local_path)
