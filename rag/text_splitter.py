
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from app.config import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents(documents: list[Document]) -> list[Document]:
    """
    Split LangChain Document objects into smaller chunks.

    Args:
        documents (list[Document]):
            List of documents returned by the PDF loader.

    Returns:
        list[Document]:
            List of chunked Document objects.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        separators=[
            "\n\n",
            "\n",
            " ",
            ""
        ],
    )

    chunks = splitter.split_documents(documents)

    return chunks
