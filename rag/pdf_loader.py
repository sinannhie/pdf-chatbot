from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

def load_pdf(pdf_path: str) -> list[Document]:
    """
    Load a PDF file and return its contents as LangChain Document objects.

    Args:
        pdf_path (str):
            Path to the PDF file.

    Returns:
        list[Document]:
            A list of Document objects, one per page.

    Raises:
        FileNotFoundError:
            If the PDF file does not exist.

        Exception:
            If the PDF cannot be loaded.
    """

    try:
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        return documents

    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    except Exception as e:
        raise Exception(f"Error loading PDF: {e}")