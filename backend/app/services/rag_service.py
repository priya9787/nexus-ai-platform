from app.services.retrieval_service import (
    RetrievalService
)

from app.services.generation_service import (
    GenerationService
)


class RAGService:

    @staticmethod
    def _can_access_point(point, user_role: str):
        if user_role == "admin":
            return True

        allowed_roles = point.payload.get("allowed_roles", [])

        return (
            user_role in allowed_roles
            or "all" in allowed_roles
        )

    @staticmethod
    def _is_no_answer(answer: str):
        normalized = answer.strip().lower()

        no_answer_phrases = [
            "i do not know",
            "i don't know",
            "do not know",
            "don't know",
            "not present",
            "not provided",
        ]

        return any(
            phrase in normalized
            for phrase in no_answer_phrases
        )

    @staticmethod
    def ask(
        query: str,
        user_role: str = "admin"
    ):

        results = RetrievalService.search(
            query,
            user_role=user_role
        )
        points = [
            point
            for point in results.points
            if RAGService._can_access_point(
                point,
                user_role
            )
        ]

        context = "\n".join(
            point.payload["text"]
            for point in points
            )
        
        sources = [
            {
                **point.payload["metadata"],
                "allowed_roles": point.payload.get("allowed_roles", [])
            }
            for point in points
            ]

        answer = (
            GenerationService.generate_response(
                query,
                context
            )
        )

        if RAGService._is_no_answer(answer):
            sources = []

        return {
            "final_response": answer,
            "sources": sources
        }
