from pydantic_settings import BaseSettings


class Settings(BaseSettings): #Create a structured configuration object
    APP_NAME: str = "NexusAI"
    APP_VERSION: str = "1.0.0" # Now every setting is typed.

    API_V1_PREFIX: str = "/api/v1"

    GROQ_API_KEY: str = "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"

    QDRANT_URL: str = ""
    REDIS_URL: str = ""
    LANGCHAIN_API_KEY: str = ""

    LANGCHAIN_PROJECT: str = ""
    LANGCHAIN_TRACING_V2: str = "false"

    class Config:
        env_file = ".env" # Load variables from .env file automatically


settings = Settings()

"""from app.core.config import settings

print(settings.APP_NAME)

OPENAI_API_KEY=abc123

settings.OPENAI_API_KEY

The confusing part is this:

class Config:
    env_file = ".env"

This does NOT magically load .env by Python itself.

When you do:

settings = Settings()

Pydantic internally does something like:

load_dotenv(".env")
"""