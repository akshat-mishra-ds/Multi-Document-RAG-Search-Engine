from langchain.tools.tavily_search import TavilySearchResults

def web_search(query):
    tool = TavilySearchResults(k=5)
    return tool.invoke(query)
