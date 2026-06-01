from fastapi import APIRouter

from app.api.v1.chat_stream import (
    router as stream_router
)

from app.api.v1.document_routes import (
    router as document_router
)

from app.api.v1.agent_routes import (
    router as agent_router
)

router = APIRouter()

router.include_router(
    stream_router,
    tags=["stream"]
)

router.include_router(
    document_router,
    tags=["documents"]
)

router.include_router(
    agent_router,
    tags=["agents"]
)