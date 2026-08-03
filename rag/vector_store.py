from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.config import CHROMA_DB_PATH
from rag.embeddings import get_embedding_model


def create_vector_store(documents: list[Document]) -> Chroma:
    """
    Create a new Chroma vector database from documents.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=CHROMA_DB_PATH,
    )

    return vector_store


def load_vector_store() -> Chroma:
    """
    Load an existing Chroma vector database.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedding_model,
    )

    return vector_store