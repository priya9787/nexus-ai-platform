from app.services.memory_service import (
    MemoryService
)

from app.agents.workflow import (
    graph
)


class AgentService:

    @staticmethod
    def run(
        session_id,
        query
    ):

        MemoryService.save_message(
            session_id,
            "user",
            query
        )
        
        history= MemoryService.get_history(session_id)

        result = graph.invoke({

            "session_id": session_id,

            "query": query,
            
            "history":history
        })

        MemoryService.save_message(

            session_id,

            "assistant",

            result["final_response"]

        )

        return {

            "final_response":
            result["final_response"],

            "sources":
            result.get(
                "sources",
                []
            ),

            "path": [

                "router",

                result.get(
                    "agent_decision"
                ),

                "critic"

            ]
        }