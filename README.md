# 🚀 AI Support Chatbot (RAG + FastAPI)

A **production-ready AI support chatbot** built using Retrieval-Augmented Generation (RAG), FastAPI, and vector databases.  
This system goes beyond basic LLM usage by integrating **context-aware responses, document ingestion, and multi-turn conversation memory**.

---

## 🔥 Features

- ⚡ **Asynchronous FastAPI backend**
- 🧠 **RAG (Retrieval-Augmented Generation) pipeline**
- 📄 **PDF & TXT document ingestion**
- 🔍 **Semantic search using vector embeddings**
- 💬 **Multi-turn conversation memory**
- 🧩 **Modular LLM architecture (Groq / OpenAI ready)**
- ✅ **Anti-hallucination guardrails**
- ⚙️ **Pydantic v2 for fast validation**

---

## 🏗️ Architecture

```
User Query
↓
Embedding (Sentence Transformers)
↓
Vector DB (ChromaDB)
↓
Top-K Context Retrieval
↓
LLM (Groq / OpenAI)
↓
Final Answer
```


---

## 🧪 API Endpoints

### 🔹 1. Chat

**POST** `/api/chat`

```json
{
  "query": "How do I reset my password?",
  "user_id": "user_123",
  "provider": "groq"
}
```

### 🔹 2. Upload Documents

**POST** `/api/upload`

- Upload PDF or TXT files
- Automatically:
  - Extracts text
  - Chunks content
  - Stores in vector DB

### 🔹 3. Ingest Text

**POST** `/api/ingest`
```json
{
  "documents": [
    "Your custom knowledge here"
  ]
}
```

## ⚙️ Tech Stack
- FastAPI – High-performance backend
- ChromaDB – Vector database
- Sentence Transformers – Embeddings
- Groq API – Ultra-fast LLM inference
- Pydantic v2 – Data validation

## 🚀 How to Run Locally
```bash
git clone <your-repo-url>
cd ai-support-chatbot

pip install -r requirements.txt

uvicorn app.main:app --reload
```

## 🌐 API Docs

- After running the server:
  - 👉 http://127.0.0.1:8000/docs

## 🔐 Environment Variables

- Create a .env file:
```bash
GROQ_API_KEY=your_api_key_here
```

## 🧠 Example Use Case
- Upload a PDF (e.g., company FAQ)
- Ask questions like:
  - "What is the refund policy?"
  - "How long is password reset valid?"
  - Get accurate, context-based answers

## 📌 Future Improvements
- 🐳 Docker deployment
- 🧠 Persistent memory (Redis / Database)
- ⚡ Streaming responses (real-time typing)
- 📊 Advanced RAG (hybrid search, metadata filtering)

## 💡 Key Highlights
- Designed with scalability and modularity in mind
- Clean separation of:
  - LLM layer
  - RAG pipeline
  - Memory system
  - Built for real-world production scenarios, not just demos

## ⭐ If you like this project

- Give it a star ⭐ and feel free to contribute!
