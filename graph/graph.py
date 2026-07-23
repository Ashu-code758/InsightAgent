from langgraph.graph import StateGraph, END

from graph.state import AgentState
from graph.nodes import *

builder = StateGraph(AgentState)

builder.add_node("collect", collect_node)
builder.add_node("analyze", analyze_node)
builder.add_node("chart", chart_node)
builder.add_node("pdf", pdf_node)

builder.set_entry_point("collect")

builder.add_edge("collect", "analyze")
builder.add_edge("analyze", "chart")
builder.add_edge("chart", "pdf")
builder.add_edge("pdf", END)

graph = builder.compile()