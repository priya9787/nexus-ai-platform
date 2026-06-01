from app.core.logger import logger

class AuditService:

    @staticmethod
    def log_event(

        user,

        action,

        metadata
    ):

        logger.info({

            "user": user,

            "action": action,

            "metadata": metadata
        })