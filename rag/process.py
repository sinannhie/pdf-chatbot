import os

from app.config import UPLOAD_FOLDER
from rag.pdf_loader import load_pdf
from rag.text_splitter import split_documents
from rag.vector_store import create_vector_store


def process_pdf(uploaded_file) -> bool:
    """
    Process an uploaded PDF and create a vector database.

    Args:
        uploaded_file:
            Streamlit UploadedFile object.

    Returns:
        bool:
            True if processing succeeds, otherwise False.
    """

    try:
        # Create upload folder if it doesn't exist
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Save uploaded PDF
        file_path = os.path.join(
            UPLOAD_FOLDER,
            uploaded_file.name
        )

        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

        # Load PDF
        documents = load_pdf(file_path)

        # Split into chunks
        chunks = split_documents(documents)

        # Create vector store
        create_vector_store(chunks)

        return True

    except Exception as error:
        print(f"Error processing PDF: {error}")
        return False