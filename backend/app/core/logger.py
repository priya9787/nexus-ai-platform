import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("nexus-ai")


"""Now anywhere:

logger.info("Application started")
prints:
2026-05-26 10:30:11 INFO Application started

"""