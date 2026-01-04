# 🔍 Multi-Document RAG Search Engine

**(Documents + Real-Time Web | Groq LLM | FAISS | Tavily | Streamlit)**

---
## 📌 Project Overview

This project implements a **Hybrid Retrieval-Augmented Generation (RAG) Search Engine** that intelligently answers user queries by combining:

* **User-uploaded documents (PDFs)**
* **Semantic vector search using FAISS**
* **Real-time web search using Tavily**
* **Large Language Model inference using Groq (LLaMA-3)**

Unlike traditional RAG systems that rely only on static documents, this system dynamically decides **when to use document knowledge, live web data, or both**, and returns **source-grounded answers with clear citations**.

This mirrors real-world enterprise AI copilots and research assistants.

---

## 🎯 Key Objectives

* Build a **multi-document semantic search engine**
* Implement **Hybrid RAG (Document + Web)**
* Enable **real-time knowledge access**
* Ensure **transparent, citation-aware answers**
* Deliver a clean, interactive **Streamlit chatbot UI**

---

## 🧠 System Architecture

```
User Query
   │
   ├── Query Router (Document / Web / Hybrid)
   │
   ├── FAISS Vector Search (Uploaded PDFs)
   │
   ├── Tavily Real-Time Web Search
   │
   ├── Context Assembly & Source Tagging
   │
   └── Groq LLM → Answer with Citations
```

---

## 🧰 Tech Stack

| Component            | Technology                        |
| -------------------- | --------------------------------- |
| Programming Language | Python                            |
| LLM                  | Groq (LLaMA-3)                    |
| LLM Orchestration    | LangChain                         |
| Embeddings           | HuggingFace Sentence Transformers |
| Vector Database      | FAISS                             |
| Web Search           | Tavily Search API                 |
| Frontend             | Streamlit                         |

---

## 📁 Project Structure

```
hybrid_rag/
│
├── app.py                     # Streamlit UI
├── config.py                  # API keys & configs
│
├── ingestion/
│   ├── loaders.py             # PDF loaders
│   ├── cleaner.py             # Text normalization
│   ├── chunker.py             # Chunking logic
│
├── vectorstore/
│   ├── faiss_index.py         # FAISS index creation & loading
│
├── retrieval/
│   ├── semantic_search.py     # Vector similarity search
│   ├── web_search.py          # Tavily web retrieval
│   ├── router.py              # Query classification
│
├── rag/
│   ├── context_builder.py     # Context construction
│   ├── qa_chain.py            # Groq RAG pipeline
│
├── models/
│   ├── schemas.py             # Unified data models
│
├── utils/
│   ├── helpers.py
│
├── requirements.txt
└── README.md
```

---

## 🔄 Workflow

1. **User uploads PDFs** via Streamlit UI
2. Documents are:

   * Cleaned
   * Chunked
   * Embedded
   * Indexed in FAISS
3. User submits a query
4. Query is classified as:

   * Document-based
   * Web-based
   * Hybrid
5. Relevant context is retrieved from:

   * FAISS
   * Tavily Web Search
6. Groq LLM generates a **grounded answer with citations**
7. Sources are transparently displayed to the user

---

## 🧪 Example Queries

* *“Explain attention mechanism in transformers”* → 📄 Document Search
* *“Latest advancements in RAG systems”* → 🌐 Web Search
* *“How does RAG compare with current LLM tools?”* → 🔀 Hybrid Search

---

## 📊 Key Features

* ✅ Multi-document semantic search
* ✅ Real-time web integration
* ✅ Hybrid query routing
* ✅ Citation-aware answer generation
* ✅ Modular, production-ready codebase
* ✅ Clean Streamlit UI

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/hybrid-rag-search-engine.git
cd hybrid-rag-search-engine
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5️⃣ Run Application

```bash
streamlit run app.py
```

---

## 📈 Evaluation Scenarios

* Static document-based knowledge retrieval
* Real-time factual queries
* Hybrid reasoning across documents and the web
* Citation clarity and source separation

---

## 🚀 Future Enhancements

* Conversational memory
* Advanced query classification using LLMs
* Re-ranking with cross-encoders
* Source confidence scoring
* Streaming responses
* User authentication & document management

---

## 🎓 Learning Outcomes

This project demonstrates:

* Hybrid RAG system design
* Enterprise-grade document retrieval
* Real-time web augmentation
* Explainable and trustworthy AI
* End-to-end LLM application development

---

## 👤 Author

**Akshat Mishra**
