from langgraph.graph import StateGraph, START, END

from .state import ResearchState
from .nodes import search_web, research, generate_answer


def build_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("search_web", search_web)
    graph.add_node("research", research)
    graph.add_node("generate_answer", generate_answer)

    graph.add_edge(START, "search_web")
    graph.add_edge("search_web", "research")
    graph.add_edge("research", "generate_answer")
    graph.add_edge("generate_answer", END)

    return graph.compile()