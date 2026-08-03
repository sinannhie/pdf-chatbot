# 🤖 AI PDF Chatbot using RAG

A production-style AI PDF Chatbot built with **LangChain**, **Google Gemini**, **ChromaDB**, and **Streamlit**.

Upload a PDF, create a vector database using Retrieval-Augmented Generation (RAG), and ask natural language questions about the document.

---

## 🚀 Features

- 📄 Upload PDF documents
- ✂️ Automatic document chunking
- 🧠 Google Gemini Embeddings
- 🗄️ ChromaDB Vector Database
- 🔍 Semantic Retrieval
- 🤖 Google Gemini LLM for Question Answering
- ⚡ Streamlit Web Interface
- ⚙️ Environment-based Configuration
- 🛡️ Error Handling
- 🧩 Modular & Production-Style Architecture

---

# 🏗️ Project Architecture

```
                User
                  │
                  ▼
             Streamlit UI
                (app.py)
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   process.py          qa_chain.py
        │                   │
        ▼                   ▼
 PDF Loader          Retriever
        │                   │
        ▼                   ▼
 Text Splitter        Prompt
        │                   │
        ▼                   ▼
 Embeddings        Gemini LLM
        │
        ▼
 ChromaDB
```

---

# 📂 Project Structure

```
pdf_chatbot/
│
├── app.py
├── .env
├── .env.example
├── requirements.txt
├── README.md
│
├── app/
│   └── config.py
│
├── rag/
│   ├── embeddings.py
│   ├── pdf_loader.py
│   ├── process.py
│   ├── prompt.py
│   ├── qa_chain.py
│   ├── retriever.py
│   ├── text_splitter.py
│   └── vector_store.py
│
└── data/
    ├── uploads/
    └── chroma_db/
```

---

# ⚙️ Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini
- Google Generative AI Embeddings
- ChromaDB
- PyPDF
- Python Dotenv

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/<your-sinannhie>/pdf-chatbot.git
```

Move into the project directory

```bash
cd pdf-chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
GOOGLE_API_KEY=your_google_api_key

LLM_MODEL=gemini-3.5-flash

EMBEDDING_MODEL=models/text-embedding-004

UPLOAD_FOLDER=./data/uploads

CHROMA_DB_PATH=./data/chroma_db

CHUNK_SIZE=1000

CHUNK_OVERLAP=200

TOP_K=4
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🔄 How It Works

1. Upload a PDF document.
2. The PDF is saved locally.
3. The document is loaded using PyPDFLoader.
4. The text is split into chunks.
5. Each chunk is converted into embeddings.
6. Embeddings are stored in ChromaDB.
7. The retriever searches the most relevant chunks.
8. Gemini generates an answer using the retrieved context.
9. The answer is displayed in the Streamlit interface.

---

# 🎯 Future Improvements

- Multiple PDF support
- Chat history
- Source citations
- Conversation memory
- Streaming responses
- Docker support
- Authentication
- Cloud deployment

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Muhammed Sinan M**

AI & Data Science Enthusiast

GitHub: https://github.com/<sinannhie>
