# 🤖 AI PDF Chatbot using RAG

A production-style AI PDF Chatbot built with **LangChain**, **Google Gemini**, **ChromaDB**, and **Streamlit**.

Upload a PDF, create a vector database using Retrieval-Augmented Generation (RAG), and ask natural language questions about your documents.

🌐 **Live Demo:** https://sinannhie-pdf-chatbot-streamlit-app-huh2nw.streamlit.app/

---

# 🚀 Features

- 📄 Upload PDF documents
- ✂️ Automatic document chunking
- 🧠 Google Gemini Embeddings
- 🗄️ ChromaDB Vector Database
- 🔍 Semantic Retrieval (RAG)
- 🤖 Google Gemini 3.6 Flash LLM
- ⚡ Streamlit Web Interface
- ⚙️ Environment-based Configuration
- 🛡️ Error Handling
- 🧩 Modular Production-Style Architecture

---

# 🏗️ Project Architecture

```
                User
                  │
                  ▼
          Streamlit Frontend
          (streamlit_app.py)
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   process.py          qa_chain.py
        │                   │
        ▼                   ▼
   PDF Loader          Retriever
        │                   │
        ▼                   ▼
 Text Splitter        Prompt Template
        │                   │
        ▼                   ▼
 Gemini Embeddings    Gemini 3.6 Flash
        │
        ▼
     ChromaDB
```

---

# 📂 Project Structure

```
pdf_chatbot/
│
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .env
├── .env.example
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
- Google Gemini API
- ChromaDB
- PyPDF
- Python Dotenv

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/sinannhie/pdf-chatbot.git
```

Move into the project

```bash
cd pdf-chatbot
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key

LLM_MODEL=gemini-3.6-flash

EMBEDDING_MODEL=gemini-embedding-001

UPLOAD_FOLDER=./data/uploads

CHROMA_DB_PATH=./data/chroma_db

CHUNK_SIZE=1000

CHUNK_OVERLAP=200

TOP_K=4
```

---

# ▶️ Run the Application

```bash
streamlit run streamlit_app.py
```

---

# 🔄 How It Works

1. Upload a PDF document.
2. Save the uploaded PDF.
3. Load the PDF using PyPDFLoader.
4. Split the document into chunks.
5. Generate embeddings using Gemini Embeddings.
6. Store embeddings in ChromaDB.
7. Retrieve the most relevant chunks using semantic search.
8. Generate answers with Gemini 3.6 Flash.
9. Display the answer in the Streamlit interface.

---

# 🌐 Live Demo

https://sinannhie-pdf-chatbot-streamlit-app-huh2nw.streamlit.app/

---

# 🎯 Future Improvements

- 📚 Multiple PDF support
- 💬 Chat history
- 📖 Source citations
- 🧠 Conversation memory
- ⚡ Streaming responses
- 🐳 Docker support
- 🔐 Authentication
- ☁️ AWS / Azure / GCP deployment

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Muhammed Sinan M**

AI & Data Science Enthusiast

GitHub: https://github.com/sinannhie

LinkedIn: https://www.linkedin.com/in/muhammed-sinan-m
