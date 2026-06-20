from typing import TypedDict, List


class AgentState(TypedDict):

    session_id: str

    query: str

    response: str

    final_response: str

    agent_decision: str
    
    history: list

    sources: List[dict]

    user_role: str
