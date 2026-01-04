from langchain_groq import ChatGroq
from config import GROQ_API_KEY, LLM_MODEL

def get_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=LLM_MODEL,
        temperature=0.2
    )

def generate_answer(context, question):
    llm = get_llm()
    prompt = f"""
Answer using ONLY the context below.
Cite sources clearly.

Context:
{context}

Question:
{question}
"""
    return llm.invoke(prompt).content
