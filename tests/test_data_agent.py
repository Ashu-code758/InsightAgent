from agents.data_agent import DataAgent


agent = DataAgent()

df = agent.collect("https://books.toscrape.com/")

print(df.head())

print("\nTotal Books :", len(df))