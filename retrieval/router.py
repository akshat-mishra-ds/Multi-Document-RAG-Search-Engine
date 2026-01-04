def route_query(query):
    realtime_keywords = ["latest", "current", "recent", "today"]

    if any(k in query.lower() for k in realtime_keywords):
        return "web"
    elif "compare" in query.lower():
        return "hybrid"
    return "document"
