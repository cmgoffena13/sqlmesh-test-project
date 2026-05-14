from sqlmesh.core.context import Context
from sqlmesh.utils import CompletionStatus

from commands.utils import retry
from config import config


@retry(attempts=5)
def run_run(context: Context) -> CompletionStatus:
    return context.run(environment="prod", skip_janitor=True)


if __name__ == "__main__":
    context = Context(config=config)
    run_status = run_run(context)
    print(f"Run Completed: {run_status}")
