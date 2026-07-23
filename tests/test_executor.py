from agents.planner import Planner
from agents.executor import Executor

planner = Planner()
executor = Executor()

plan = planner.plan(
    "Analyze books website and generate charts."
)

executor.execute(plan)