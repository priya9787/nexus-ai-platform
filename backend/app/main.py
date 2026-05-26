from fastapi import FastAPI
from app.core.config import settings
# from app.api.v1.router import router
from app.core.exceptions import (AppException,app_exception_handler)
from app.middleware.logging import LoggingMiddleware
from app.api.v1.document_routes import router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.add_exception_handler(AppException,app_exception_handler)

app.add_middleware(LoggingMiddleware)

# @app.get("/")
# async def root():
#     return {
#         "message": "NexusAI Backend Running"
#     }

app.include_router( #Attach router to main app with prefix api/v1 - health - api/v1/health
    router, 
    prefix=settings.API_V1_PREFIX
)