from langgraph.graph import StateGraph, END

from app.agents.state import AgentState

from app.agents.router_agent import (
    router_agent
)

from app.agents.retrieval_agent import (
    retrieval_agent
)

from app.agents.summarizer_agent import (
    summarizer_agent
)

from app.agents.critic_agent import (
    critic_agent
)


workflow = StateGraph(AgentState)

workflow.add_node(
    "router",
    router_agent
)

workflow.add_node(
    "retrieval",
    retrieval_agent
)

workflow.add_node(
    "summarizer",
    summarizer_agent
)

workflow.add_node(
    "critic",
    critic_agent
)

workflow.set_entry_point("router")

def route_decision(state):

    if state["agent_decision"] == "summarization":
        return "summarizer"

    return "retrieval"

workflow.add_conditional_edges(
    "router",
    route_decision,
    {
        "retrieval": "retrieval",
        "summarizer": "summarizer"
    }
)

workflow.add_edge(
    "retrieval",
    "critic"
)

workflow.add_edge(
    "summarizer",
    "critic"
)

workflow.add_edge(
    "critic",
    END
)

graph = workflow.compile()