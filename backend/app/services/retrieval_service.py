from app.services.embedding_service import (
    EmbeddingService
)

from app.services.vector_db_service import (
    VectorDBService
)


class RetrievalService:

    @staticmethod
    def search(query: str):

        query_embedding = (
            EmbeddingService.model.encode(query)
        )

        results = (
            VectorDBService.client.query_points(
                collection_name="documents",
                query=query_embedding.tolist(),
                limit=5
            )
        )

        return results