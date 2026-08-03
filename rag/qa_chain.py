from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import GOOGLE_API_KEY, LLM_MODEL
from rag.prompt import get_prompt_template
from rag.retriever import create_retriever


def get_qa_chain():
    """
    Create the complete RAG question-answering chain.
    """

    retriever = create_retriever()

    prompt = get_prompt_template()

    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=GOOGLE_API_KEY,
    )

    qa_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return qa_chain