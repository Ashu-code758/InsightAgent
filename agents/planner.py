import json
from tools.ai_tool import AITool


class Planner:

    def __init__(self):
        self.ai = AITool()

    def plan(self, user_request):

        prompt = f"""
You are an AI Agent Planner.

Available tools:

1. browser
   - Opens website

2. scraper
   - Extracts structured data

3. ai
   - Analyze dataframe

4. chart
   - Generate charts

Return ONLY valid JSON.

Example:

{{
    "steps":[
        "browser",
        "scraper",
        "ai",
        "chart"
    ]
}}

User Request:
{user_request}
"""

        response = self.ai.ask(prompt)

        return json.loads(response)