from agents.data_agent import DataAgent


class Executor:

    def __init__(self):
        self.agent = DataAgent()

    def execute(self, plan, url):

        state = {}

        print("\n🚀 Executing AI Plan...\n")

        for step in plan["steps"]:

            print(f"➡ {step}")

            if step == "browser":
                print("🌐 Browser Ready")

            elif step == "scraper":
                df = self.agent.collect(url)
                state["dataframe"] = df
                print(f"✅ Scraped {len(df)} records")

            elif step == "ai":
                analysis = self.agent.analyze(state["dataframe"])
                state["analysis"] = analysis
                print("✅ AI Analysis Completed")

            elif step == "chart":
                self.agent.visualize(state["dataframe"])
                print("📊 Charts Generated")

        return state