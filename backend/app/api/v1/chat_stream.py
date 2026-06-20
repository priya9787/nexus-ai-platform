from fastapi import APIRouter

from sse_starlette.sse import (
    EventSourceResponse
)

import asyncio
import json

from app.services.agent_service import (
    AgentService
)

router = APIRouter()


@router.get("/stream")

async def stream_chat(
    query: str,
    session_id: str ='test-session',
    role: str = "admin"
):

    async def event_generator():
        
        print("generator started")

        result = await asyncio.to_thread(
            AgentService.run,
            session_id,
            query,
            role.lower()
        )
        
        print("agent finished")

        yield {
            "event": "path",
            "data": json.dumps(result.get("path", []))
        }

        yield {
            "event": "sources",
            "data": json.dumps(result.get("sources", []))
        }

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

        yield {
            "event": "done",
            "data": "ok"
        }

    return EventSourceResponse(
        event_generator()
    )
