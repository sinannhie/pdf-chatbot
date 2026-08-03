from langchain_core.prompts import PromptTemplate


def get_prompt_template() -> PromptTemplate:
    """
    Create the prompt template used for the RAG pipeline.
    """

    template = """
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not available in the context, simply say:

"I couldn't find the answer in the provided document."

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""

    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"],
    )

    return prompt