from app.services.memory_service import (
    MemoryService
)

from app.services.rag_service import (
    RAGService
)


def retrieval_agent(state):

    history = MemoryService.get_history(
        state["session_id"]
    )
    

    query = state["query"]

    enriched_query = f"""

    History:

    {history}

    Current Query:

    {query}

    """

    result = RAGService.ask(
        enriched_query,
        user_role=state.get("user_role", "admin")
    )

    return {
        "response": result["final_response"],
        "sources": result.get("sources", [])
    }
