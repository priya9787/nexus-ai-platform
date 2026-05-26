from app.services.document_loader import (
    DocumentLoaderService
)

from app.services.chunking_service import (
    ChunkingService
)

from app.services.embedding_service import (
    EmbeddingService
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

        return {
            "documents": documents,
            "chunks": chunks,
            "embeddings": embeddings
        }