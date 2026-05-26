from sentence_transformers import SentenceTransformer


class EmbeddingService:

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    @classmethod
    def generate_embeddings(cls, chunks):

        texts = [
            chunk.page_content
            for chunk in chunks
        ]

        embeddings = cls.model.encode(texts)

        return embeddings