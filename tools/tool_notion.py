import os
from notion_client import Client

def create_client():
    api_token = os.getenv("NOTION_TOKEN")
    return Client(auth=api_token, log_level=3) # 3 = INFO

def tool_get_page_info(page_id:str):
    """
    A tool that fetches page information about a given notion page.

    Example response:
    {
        "object": "page",
        "id": "a19b316f-0b8d-4514-b21b-282430dbeac0",
        "created_time": "2023-10-05T23:07:00.000Z",
        "last_edited_time": "2025-03-25T18:08:00.000Z",
        "created_by": {
            "object": "user",
            "id": "6942e4ef-9119-4b5b-93b2-03652d4866f4"
        },
        "last_edited_by": {
            "object": "user",
            "id": "6942e4ef-9119-4b5b-93b2-03652d4866f4"
        },
        "cover": {
            "type": "external",
            "external": {
                "url": "https://www.notion.so/images/page-cover/gradients_8.png"
            }
        },
        "icon": {
            "type": "emoji",
            "emoji": "👟"
        },
        "parent": {
            "type": "block_id",
            "block_id": "12ec614c-ae0d-80da-8243-d07350845fef"
        },
        "archived": false,
        "in_trash": false,
        "properties": {
            "title": {
                "id": "title",
                "type": "title",
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Outings",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Outings",
                        "href": null
                    }
                ]
            }
        },
        "url": "https://www.notion.so/Outings-a19b316f0b8d4514b21b282430dbeac0",
        "public_url": null,
        "developer_survey": "https://notionup.typeform.com/to/bllBsoI4?utm_source=postman",
        "request_id": "532cc04d-a7b4-4ec2-ab0e-0f0813092d4f"
    }

    """
    notion = create_client()
    page_info = notion.pages.retrieve(page_id=page_id)
    notion.close()
    return page_info

def tool_get_page_contents(page_id:str):
    """
    A tool that fetches all of the blocks of content for a given page_id.
    """
    notion = create_client()
    content_blocks = notion.blocks.children.list(block_id=page_id)
    notion.close()

    return content_blocks