import streamlit as st
import tempfile
from ingestion.loaders import load_pdf
from ingestion.chunker import chunk_documents
from vectorstore.faiss_index import build_index, load_index
from retrieval.semantic_search import search_docs
from retrieval.web_search import web_search
from retrieval.router import route_query
from rag.context_builder import build_context
from rag.qa_chain import generate_answer

st.set_page_config("Hybrid RAG", layout="wide")
st.title("📚 Hybrid RAG Search Engine")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDFs", type="pdf", accept_multiple_files=True
)

if uploaded_files:
    all_docs = []
    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(file.read())
            docs = load_pdf(tmp.name)
            all_docs.extend(docs)

    chunks = chunk_documents(all_docs)
    db = build_index(chunks)
    st.sidebar.success("Documents indexed!")

query = st.text_input("Ask your question")

if query:
    db = load_index()
    route = route_query(query)

    docs = search_docs(db, query)

    web_results = web_search(query) if route in ["web", "hybrid"] else None

    context = build_context(docs, web_results)
    answer = generate_answer(context, query)

    st.markdown("### 🧠 Answer")
    st.write(answer)
