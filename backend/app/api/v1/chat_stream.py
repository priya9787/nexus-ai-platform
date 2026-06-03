from fastapi import APIRouter

from sse_starlette.sse import (
    EventSourceResponse
)

import asyncio

from app.services.agent_service import (
    AgentService
)

router = APIRouter()


@router.get("/stream")

async def stream_chat(
    query: str,
    session_id: str ='test-session'
):

    async def event_generator():
        
        print("generator started")

        result = await asyncio.to_thread(AgentService.run,session_id,query)
        
        print("agent finished")

        response = result[
            "final_response"
        ]

        for word in response.split():

            yield {
                "data": word + " "
            }

            await asyncio.sleep(
                0.03
            )

    return EventSourceResponse(
        event_generator()
    )