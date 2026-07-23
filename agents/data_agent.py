from tools.browser import BrowserTool
from tools.scraper import ScraperTool
from tools.chart_tool import ChartTool
from tools.ai_tool import AITool
from tools.pdf_tool import PDFTool
import os
import pandas as pd



class DataAgent:

    def __init__(self):
        self.browser = BrowserTool()
        self.scraper = ScraperTool()
        self.ai = AITool()
        self.chart = ChartTool()
        self.pdf = PDFTool()

    def collect(self, url):

        self.browser.start()

        self.browser.open(url)

        html = self.browser.html()

        soup = self.scraper.parse(html)

        books = []

        cards = soup.select("article.product_pod")

        for card in cards:

            title = card.h3.a["title"]
            price = card.select_one(".price_color").text
            availability = card.select_one(".availability").text.strip()

            books.append({
                "Title": title,
                "Price": price,
                "Availability": availability
            })

        self.browser.close()

        os.makedirs("data", exist_ok=True)

        df = pd.DataFrame(books)

        df.to_csv("data/books.csv", index=False)

        return df

    def analyze(self, dataframe):

        prompt = f"""
You are an expert Data Analyst.

Analyze the following dataset:

{dataframe.to_string(index=False)}

Provide:

1. Total number of records
2. Price analysis
3. Availability analysis
4. Interesting insights
5. Overall summary
"""

        return self.ai.ask(prompt)

    def generate_report(self, dataframe):

        analysis = self.analyze(dataframe)

        pdf_path = self.pdf.create_report(analysis)

        return pdf_path

    def visualize(self, dataframe):

        self.chart.bar_chart(dataframe)
        self.chart.price_chart(dataframe)

        return "Charts Generated Successfully"