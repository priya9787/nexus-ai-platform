from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from app.core.config import settings


class VectorDBService:

    COLLECTION_NAME = "documents"
    client = QdrantClient(
        host="localhost",
        port=6333
    )


    @classmethod
    def create_collection(cls):

        cls.client.recreate_collection(
            collection_name=cls.COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

    @classmethod
    def store_embeddings(
        cls,
        chunks,
        embeddings
    ):

        points = []

        for idx, (chunk, embedding) in enumerate(
            zip(chunks, embeddings)
        ):

            points.append(
                PointStruct(
                    id=idx,
                    vector=embedding.tolist(),
                    payload={
                        "text": chunk.page_content,
                        "metadata": chunk.metadata
                    }
                )
            )

        cls.client.upsert(
            collection_name=cls.COLLECTION_NAME,
            points=points
        )    