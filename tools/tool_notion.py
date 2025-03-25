import os
from notion_client import Client

def create_client():
    api_token = os.getenv("NOTION_TOKEN")
    return Client(auth=api_token, log_level=3)

def tool_retrieve_page(page_id:str):
    """
    A tool to interact with the notion application, specifically fetch a page using it's id
    """
    notion = create_client()
    #return notion.pages.retrieve(page_id=page_id)
    return notion.search(query="vape store").get("results")
    #return notion.users.list()