def build_context(docs, web_results=None):
    context = ""

    for d in docs:
        context += f"[Doc] {d.metadata.get('source')}:\n{d.page_content}\n\n"

    if web_results:
        for w in web_results:
            context += f"[Web] {w['title']}:\n{w['content']}\n\n"

    return context
