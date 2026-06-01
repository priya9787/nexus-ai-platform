from fastapi import FastAPI
from app.core.config import settings
# from app.api.v1.router import router
from app.core.exceptions import (AppException,app_exception_handler)
from app.middleware.logging import LoggingMiddleware
from app.api.v1.router import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.add_exception_handler(AppException,app_exception_handler)

app.add_middleware(LoggingMiddleware)
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# @app.get("/")
# async def root():
#     return {
#         "message": "NexusAI Backend Running"
#     }

app.include_router( #Attach router to main app with prefix api/v1 - health - api/v1/health
    router, 
    prefix=settings.API_V1_PREFIX
)