from sqlmesh.core.context import Context

from commands.utils import retry
from config import config


@retry(attempts=2)
def run_janitor(context: Context) -> bool:
    return context.run_janitor(ignore_ttl=False)


if __name__ == "__main__":
    context = Context(config=config)
    janitor_status = run_janitor(context)
    print(f"Janitor Completed: {janitor_status}")
