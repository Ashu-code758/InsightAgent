from agents.data_agent import DataAgent

agent = DataAgent()

df = agent.collect("https://books.toscrape.com/")

pdf = agent.generate_report(df)

print("PDF Generated:", pdf)