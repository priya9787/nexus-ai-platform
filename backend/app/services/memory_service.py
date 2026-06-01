import json

from app.db.redis_client import (
    redis_client
)


class MemoryService:

    @staticmethod
    def save_message(
        session_id,
        role,
        content
    ):

        memory_key = f"chat:{session_id}"

        existing = redis_client.get(
            memory_key
        )

        history = []

        if existing:

            history = json.loads(
                existing
            )

        history.append({
            "role": role,
            "content": content
        })

        redis_client.set(
            memory_key,
            json.dumps(history),
            ex=86400 #Memory auto-expires. TTL 24 hours - 86400 seconds

        )

    @staticmethod
    def get_history(
        session_id
    ):

        memory_key = f"chat:{session_id}"

        history = redis_client.get(
            memory_key
        )

        if not history:
            return []

        return json.loads(history)