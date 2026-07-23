from tools.browser import BrowserTool
from tools.scraper import ScraperTool
from tools.ai_tool import AITool
from tools.chart_tool import ChartTool

TOOLS = {
    "browser": BrowserTool(),
    "scraper": ScraperTool(),
    "ai": AITool(),
    "chart": ChartTool()
}