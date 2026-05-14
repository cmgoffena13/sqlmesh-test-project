from sqlmesh.core.context import Context
from sqlmesh.core.plan.definition import Plan

from commands.utils import retry
from config import config


@retry(attempts=2)
def run_plan(context: Context) -> Plan:
    p = context.plan(environment="prod", auto_apply=True, no_prompts=True)
    context.apply(p)
    return p


if __name__ == "__main__":
    context = Context(config=config)
    plan = run_plan(context)
    print(f"Plan Completed: {plan}")
