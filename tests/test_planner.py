from agents.planner import Planner

planner = Planner()

plan = planner.plan(
    "Analyze books website and generate charts."
)

print(plan)