from app.services.retrieval_service import (
    RetrievalService
)

from app.services.bm25_service import (
    BM25Service
)


class HybridRetrievalService:

    @staticmethod
    def hybrid_search(query):

        vector_results = (
            RetrievalService.search(query)
        )

        bm25_results = (
            BM25Service.search(query)
        )

        combined_results = []

        seen = set()

        for result in vector_results:

            text = result.payload["text"]

            if text not in seen:
                combined_results.append(text)
                seen.add(text)

        for result in bm25_results:

            if result.page_content not in seen:
                combined_results.append(
                    result.page_content
                )
                seen.add(result.page_content)

        return combined_results[:5]