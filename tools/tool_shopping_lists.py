import os
from tools.tool_notion import tool_get_page_contents

def tool_shoping_lists():
    """
    A set of scripts to build on-top-of tool_notion to surface shoppings lists (add/update)
    """
    SHOPPING_LIST_PAGE_ID=os.getenv("SHOPPING_LIST_PAGE_ID")
    results = tool_get_page_contents(SHOPPING_LIST_PAGE_ID)

    ## TODO: Get the list of headings, ideally using some sorta jsonpath
    h2_path = "$.results[*].heading_2[*][0].plain_text"