import os
from tavily import TavilyClient

def tool_search(query:str) -> str:
    """ 
    Search online using the given query. 
    Returning a set of reasults, each with a score 0-1 based on relevance to the query
    
    eg. (
        { 
            "title": "XYZ", 
            "url": "https://www.....", 
            "content": "Some text and stuff...",
            "score": 0.9, 
        }, 
    )
    """
    api_key = os.getenv("TAVILY_KEY")
    tavily_client = TavilyClient(api_key=api_key)
    response = tavily_client.search(query)
    return response