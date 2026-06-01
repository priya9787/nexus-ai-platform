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
    def process_document(file_path: str):

        documents = (
            DocumentLoaderService.load_pdf(file_path)
        )

        chunks = (
            ChunkingService.chunk_documents(documents)
        )

        embeddings = (
            EmbeddingService.generate_embeddings(chunks)
        )
        
        VectorDBService.create_collection()

        VectorDBService.store_embeddings(
            chunks,
            embeddings
        )

        return {
            "documents": documents,
            "chunks": chunks,
            "embeddings": embeddings,
            "chunks":len(chunks)
        }