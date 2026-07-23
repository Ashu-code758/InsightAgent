from agents.data_agent import DataAgent

agent = DataAgent()

def collect_node(state):
    print("✅ Collect Node")
    df = agent.collect(state["url"])
    state["dataframe"] = df
    return state


def analyze_node(state):
    print("✅ Analyze Node")
    state["analysis"] = agent.analyze(state["dataframe"])
    return state


def chart_node(state):
    print("✅ Chart Node")
    agent.visualize(state["dataframe"])
    return state


def pdf_node(state):
    print("✅ PDF Node")
    state["pdf"] = agent.generate_report(state["dataframe"])
    return state