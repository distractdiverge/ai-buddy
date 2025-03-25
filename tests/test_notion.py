import pytest
from dotenv import load_dotenv
from tools.tool_notion import tool_get_page_info, tool_get_page_contents

###
### This is an integration test, not a unit test, it calls out!!!!
###

def setup_function(function):
    load_dotenv()

def test_get_page_info():
    page_id = "a19b316f0b8d4514b21b282430dbeac0"
    formatted_page_id = "a19b316f-0b8d-4514-b21b-282430dbeac0"
    result = tool_get_page_info(page_id)
    
    assert result is not None

    object_type = result["object"]
    object_id = result["id"]
    
    assert object_type == "page"
    assert object_id == formatted_page_id

def test_get_page_contents():
    page_id = "a19b316f0b8d4514b21b282430dbeac0"
    formatted_page_id = "a19b316f-0b8d-4514-b21b-282430dbeac0"
    result = tool_get_page_contents(page_id)
    
    assert result is not None

    object_type = result["object"]
    blocks = result["results"]
    
    assert object_type == "list"
    assert len(blocks) > 0