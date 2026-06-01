import time

from app.core.logger import logger


def track_latency(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(
            *args,
            **kwargs
        )

        duration = (
            time.time()
            - start
        )

        logger.info(
            f"{func.__name__} "
            f"{duration:.2f}s"
        )

        return result

    return wrapper