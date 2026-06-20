from app.services.embedding_service import (
    EmbeddingService
)

from app.services.vector_db_service import (
    VectorDBService
)

from qdrant_client.models import (
    FieldCondition,
    Filter,
    MatchAny
)


class RetrievalService:

    @staticmethod
    def search(
        query: str,
        user_role: str = "admin"
    ):

        query_embedding = (
            EmbeddingService.model.encode(query)
        )

        access_filter = None

        if user_role != "admin":
            access_filter = Filter(
                must=[
                    FieldCondition(
                        key="allowed_roles",
                        match=MatchAny(any=[user_role, "all"])
                    )
                ]
            )

        results = (
            VectorDBService.client.query_points(
                collection_name="documents",
                query=query_embedding.tolist(),
                query_filter=access_filter,
                limit=5
            )
        )

        return results
