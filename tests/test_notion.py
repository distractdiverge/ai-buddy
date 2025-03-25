import pytest
from dotenv import load_dotenv
from tools.tool_notion import tool_retrieve_page

def setup_function(function):
    load_dotenv()

def test_tool_retrive_page():
    page_id = "a19b316f0b8d4514b21b282430dbeac0"
    formatted_page_id = "a19b316f-0b8d-4514-b21b-282430dbeac0"
    result = tool_retrieve_page(page_id)
    
    assert result is not None

    object_type = result["object"]
    object_id = result["id"]
    
    assert object_type == "page"
    assert object_id == formatted_page_id