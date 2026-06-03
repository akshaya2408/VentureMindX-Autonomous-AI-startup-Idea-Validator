from copy import deepcopy

from langgraph.graph import StateGraph

from database.report_collection import save_report
from vector_db.startup_rag import store_startup_research


# -------------------------
# 1. Build Graph (IMPORTANT)
# -------------------------
def build_graph():
    graph = StateGraph(dict)

    # Example node (replace with your real logic)
    def analyze_node(state):
        idea = state["idea"]

        # 👉 Replace this with your real AI / LLM logic
        result = {
            "summary": f"Analysis of {idea}",
            "score": 7.5,
            "market_fit": "medium"
        }

        return {**state, "result": result}

    graph.add_node("analyze", analyze_node)

    graph.set_entry_point("analyze")
    graph.set_finish_point("analyze")

    return graph.compile()


# Compile once (IMPORTANT for performance)
app = build_graph()


# -------------------------
# 2. Main Function
# -------------------------
def analyze_startup(idea):

    try:
        # -------------------------
        # Run LangGraph workflow
        # -------------------------
        result = app.invoke({"idea": idea})

        if not result:
            return {
                "success": False,
                "error": "Graph returned empty result"
            }

        # -------------------------
        # Prepare report
        # -------------------------
        report = deepcopy(result)
        report["idea"] = idea

        response_report = deepcopy(report)

        # -------------------------
        # Save to MongoDB
        # -------------------------
        report_id = save_report(report)

        # -------------------------
        # Save to ChromaDB
        # -------------------------
        store_startup_research(
            startup_id=str(report_id),
            idea=idea,
            report=str(report)
        )

        # -------------------------
        # Attach ID
        # -------------------------
        response_report["report_id"] = str(report_id)

        return {
            "success": True,
            "data": response_report
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }