from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from config import FAISS_PATH, EMBED_MODEL

def build_index(docs):
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(FAISS_PATH)
    return db

def load_index():
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    return FAISS.load_local(FAISS_PATH, embeddings)
