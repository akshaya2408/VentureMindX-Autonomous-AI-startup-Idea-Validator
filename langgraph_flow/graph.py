from langgraph.graph import StateGraph, END
from agents_graph.state import StartupState

from agents.market_agent import market_analysis
from agents.competitor_agent import competitor_analysis
from agents.persona_agent import generate_personas
from agents.swot_agent import swot_analysis
from agents.viability_agent import viability_score
from agents.revenue_agent import revenue_forecast
from agents.investor_agent import investor_readiness


# ---------------- PARALLEL NODES ----------------

def market_node(state: StartupState):
    return {"market": market_analysis(state["idea"])}

def competitor_node(state: StartupState):
    return {"competitors": competitor_analysis(state["idea"])}

def persona_node(state: StartupState):
    return {"personas": generate_personas(state["idea"])}


def swot_node(state: StartupState):
    return {"swot": swot_analysis(state["idea"])}

def viability_node(state: StartupState):
    return {"viability": viability_score(state["idea"])}

def revenue_node(state: StartupState):
    return {"revenue": revenue_forecast(state["idea"])}

def investor_node(state: StartupState):
    return {"investor": investor_readiness(state["idea"])}


# ---------------- ROUTER NODE (IMPORTANT FIX) ----------------

def fanout_node(state: StartupState):
    # This is just a pass-through trigger node
    return state


# ---------------- GRAPH ----------------

graph = StateGraph(StartupState)

graph.add_node("start", fanout_node)

graph.add_node("market", market_node)
graph.add_node("competitor", competitor_node)
graph.add_node("persona", persona_node)

graph.add_node("swot", swot_node)
graph.add_node("viability", viability_node)
graph.add_node("revenue", revenue_node)
graph.add_node("investor", investor_node)


# Entry point
graph.set_entry_point("start")


# ---------------- PARALLEL EXECUTION FIX ----------------
graph.add_edge("start", "market")
graph.add_edge("start", "competitor")
graph.add_edge("start", "persona")


# All converge
graph.add_edge("market", "swot")
graph.add_edge("competitor", "swot")
graph.add_edge("persona", "swot")


# Pipeline flow
graph.add_edge("swot", "viability")
graph.add_edge("viability", "revenue")
graph.add_edge("revenue", "investor")
graph.add_edge("investor", END)


graph = graph.compile()


def run_graph(idea: str):
    return graph.invoke({"idea": idea})