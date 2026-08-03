from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import GOOGLE_API_KEY, EMBEDDING_MODEL


def get_embedding_model() -> GoogleGenerativeAIEmbeddings:
    """
    Create and return the Google embedding model.

    Returns:
        GoogleGenerativeAIEmbeddings:
            Configured embedding model.
    """

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY
    )

    return embeddings