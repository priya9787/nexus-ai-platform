from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

import uuid

from app.core.config import settings


class VectorDBService:

    COLLECTION_NAME = "documents"
    client = QdrantClient(
        host="localhost",
        port=6333
    )


    @classmethod
    def create_collection(cls):
        if cls.client.collection_exists(
            collection_name=cls.COLLECTION_NAME
        ):
            return

        cls.client.create_collection(
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
        embeddings,
        allowed_roles
    ):

        points = []

        for idx, (chunk, embedding) in enumerate(
            zip(chunks, embeddings)
        ):

            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding.tolist(),
                    payload={
                        "text": chunk.page_content,
                        "metadata": chunk.metadata,
                        "allowed_roles": allowed_roles
                    }
                )
            )

        cls.client.upsert(
            collection_name=cls.COLLECTION_NAME,
            points=points
        )    
