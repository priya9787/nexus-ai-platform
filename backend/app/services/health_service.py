class HealthService:

    @staticmethod
    async def get_status():

        return {
            "status": "running"
        }