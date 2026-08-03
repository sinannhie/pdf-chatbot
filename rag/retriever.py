from langchain_core.vectorstores import VectorStoreRetriever

from rag.vector_store import load_vector_store
from app.config import TOP_K


def create_retriever() -> VectorStoreRetriever:
    """
    Create a retriever from the existing vector store.
    """

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K},
    )

    return retriever