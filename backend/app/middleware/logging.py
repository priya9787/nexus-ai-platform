import time

from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start_time = time.time() #stores request start time.

        response = await call_next(request)

        process_time = time.time() - start_time #calculates API latency.

        logger.info(
            f"{request.method} {request.url.path} "
            f"completed in {process_time:.4f}s"
        )

        return response