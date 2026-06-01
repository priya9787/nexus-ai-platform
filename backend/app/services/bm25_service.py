from rank_bm25 import BM25Okapi


class BM25Service:

    bm25 = None
    documents = []

    @classmethod
    def initialize(cls, chunks):

        cls.documents = chunks

        tokenized_docs = [
            chunk.page_content.split()
            for chunk in chunks
        ]

        cls.bm25 = BM25Okapi(tokenized_docs)

    @classmethod
    def search(cls, query, top_k=5):

        tokenized_query = query.split()

        results = cls.bm25.get_top_n(
            tokenized_query,
            cls.documents,
            n=top_k
        )

        return results