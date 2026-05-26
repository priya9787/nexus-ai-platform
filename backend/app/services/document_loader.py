from langchain_community.document_loaders import PyPDFLoader


class DocumentLoaderService:

    @staticmethod
    def load_pdf(file_path: str):

        loader = PyPDFLoader(file_path)

        documents = loader.load()

        return documents
    
"""  loader.load()  return 
[
    Document(
        page_content="PDF text...",
        metadata={
            "page": 1,
            "source": "file.pdf"
        }
    )
]"""    