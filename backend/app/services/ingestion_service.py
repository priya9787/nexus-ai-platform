from app.services.document_loader import (
    DocumentLoaderService
)

from app.services.chunking_service import (
    ChunkingService
)

from app.services.embedding_service import (
    EmbeddingService
)

from app.services.vector_db_service import (
    VectorDBService
)



class IngestionService:

    @staticmethod
    def process_document(
        file_path: str,
        allowed_roles=None
    ):
        allowed_roles = allowed_roles or ["admin"]

        documents = (
            DocumentLoaderService.load_pdf(file_path)
        )

        for document in documents:
            document.metadata["allowed_roles"] = allowed_roles

        chunks = (
            ChunkingService.chunk_documents(documents)
        )

        embeddings = (
            EmbeddingService.generate_embeddings(chunks)
        )
        
        VectorDBService.create_collection()

        VectorDBService.store_embeddings(
            chunks,
            embeddings,
            allowed_roles
        )

        return {
            "documents": documents,
            "chunks": chunks,
            "embeddings": embeddings,
            "chunks":len(chunks)
        }
