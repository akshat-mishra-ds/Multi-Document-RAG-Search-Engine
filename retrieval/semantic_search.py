def search_docs(db, query, k=5):
    return db.similarity_search(query, k=k)
