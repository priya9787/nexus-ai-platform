from fastapi import APIRouter

from app.services.agent_service import (
    AgentService
)

router = APIRouter()


@router.post("/agent")

async def run_agent(query: str,session_id: str = "test-session"):

    result = AgentService.run(session_id,query)

    return result