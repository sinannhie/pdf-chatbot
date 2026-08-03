
import os

from dotenv import load_dotenv

load_dotenv()


# Google AI Configuration

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")



# Storage Configuration

CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")


# RAG Configuration

CHUNK_SIZE = os.getenv("CHUNK_SIZE", "1000")
CHUNK_OVERLAP = os.getenv("CHUNK_OVERLAP", "200")

# Retrieval Configuration

TOP_K = os.getenv("TOP_K", "4")


# Validate Required Environment Variables (Fail Fast)

required_settings = {
    "GOOGLE_API_KEY": GOOGLE_API_KEY,
    "LLM_MODEL": LLM_MODEL,
    "EMBEDDING_MODEL": EMBEDDING_MODEL,
    "CHROMA_DB_PATH": CHROMA_DB_PATH,
    "UPLOAD_FOLDER": UPLOAD_FOLDER,
}

missing_settings = [
    key
    for key, value in required_settings.items()
    if not value
]

if missing_settings:
    raise ValueError(
        f"Missing required environment variables: {', '.join(missing_settings)}"
    )



# Convert RAG Configuration


try:
    CHUNK_SIZE = int(CHUNK_SIZE)
    CHUNK_OVERLAP = int(CHUNK_OVERLAP)
    TOP_K = int(TOP_K)

except ValueError:
    raise ValueError(
        "CHUNK_SIZE, CHUNK_OVERLAP and TOP_K must be valid integers."
    )

# Validate RAG Configuration

if CHUNK_SIZE <= 0:
    raise ValueError(
        "CHUNK_SIZE must be greater than 0."
    )

if CHUNK_OVERLAP < 0:
    raise ValueError(
        "CHUNK_OVERLAP cannot be negative."
    )

if CHUNK_OVERLAP >= CHUNK_SIZE:
    raise ValueError(
        "CHUNK_OVERLAP must be smaller than CHUNK_SIZE."
    )

#validat rag configuration

if TOP_K <= 0:
    raise ValueError(
        "TOP_K must be greater than 0."
    )