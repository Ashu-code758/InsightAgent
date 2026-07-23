from agents.planner import Planner
from agents.executor import Executor

planner = Planner()
executor = Executor()

user_request = "Analyze books website and generate charts."

plan = planner.plan(user_request)

result = executor.execute(
    plan,
    "https://books.toscrape.com/"
)

print("\n=========================")
print("FINAL ANALYSIS")
print("=========================\n")

print(result["analysis"])