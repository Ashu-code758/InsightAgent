from agents.data_agent import DataAgent

agent = DataAgent()

df = agent.collect("https://books.toscrape.com/")

print(agent.visualize(df))