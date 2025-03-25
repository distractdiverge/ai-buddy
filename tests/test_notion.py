import pytest
from dotenv import load_dotenv
from tools.tool_notion import tool_retrieve_page

def setup_function(function):
    load_dotenv()

def test_tool_retrive_page():
    page_id = "a19b316f0b8d4514b21b282430dbeac0"
    result = tool_retrieve_page(page_id)
    assert result == None