import os
from tavily import TavilyClient

def tool_browse(url:str) -> str:
    """ 
    Browse online using the given url. 
    """
    api_key = os.getenv("TAVILY_KEY")
    tavily_client = TavilyClient(api_key=api_key)
    response = tavily_client.extract(url)
    print(response)
    return response