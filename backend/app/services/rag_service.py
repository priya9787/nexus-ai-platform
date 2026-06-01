from app.services.retrieval_service import (
    RetrievalService
)

from app.services.generation_service import (
    GenerationService
)


class RAGService:

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

        return {
            "final_response": answer,
            "sources": sources
        }