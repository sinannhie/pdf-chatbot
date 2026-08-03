import streamlit as st

from rag.process import process_pdf
from rag.qa_chain import get_qa_chain


# Configure Streamlit Page


st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="🤖",
    layout="wide",
)


# Application Title


st.title("🤖 AI PDF Chatbot")

st.write(
    "Upload a PDF, process it, and ask questions about its content."
)


# Session State Initialization


if "processed" not in st.session_state:
    st.session_state.processed = False

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None


# Sidebar


with st.sidebar:

    st.header("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
    )

    if st.button("⚙️ Process PDF"):

        if uploaded_file:

            try:

                with st.spinner("Processing PDF..."):

                    process_pdf(uploaded_file)

                    st.session_state.qa_chain = get_qa_chain()

                    st.session_state.processed = True

                st.success("✅ PDF processed successfully!")

            except Exception as e:

                st.session_state.processed = False
                st.session_state.qa_chain = None

                st.error(
                    f"❌ Error processing PDF: {e}"
                )

        else:

            st.warning("⚠️ Please upload a PDF first.")


# Question Answering


st.header("💬 Ask Questions")

question = st.text_input(
    "Ask a question about your PDF"
)

if question:

    if st.session_state.processed:

        try:

            with st.spinner("Generating answer..."):

                response = st.session_state.qa_chain.invoke(question)

            st.markdown("### 🤖 Answer")

            st.write(response)

        except Exception as e:

            st.error(
                f"❌ Error generating answer: {e}"
            )

    else:

        st.warning("⚠️ Please process a PDF first.")