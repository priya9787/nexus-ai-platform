from app.services.retrieval_service import (
    RetrievalService
)

from app.services.generation_service import (
    GenerationService
)


class RAGService:

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
    def ask(query: str):

        results = RetrievalService.search(query)
        points = results.points

        context = "\n".join(
            point.payload["text"]
            for point in points
            )
        
        sources = [
            point.payload["metadata"]
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
