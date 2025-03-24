import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import lmstudio as lms

from tavily import TavilyClient

from dotenv import load_dotenv

def load_model():
    # TODO: Work on this, it may be trying to load the model directly instead of via LMStudio
    model_name = "qwen2.5-0.5b-instruct-mlx"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
 

def tool_multiply(a: float, b: float) -> float:
    """Given two numbers a and b, returns the product of them"""
    return a * b

def chat_with_ai(message: str) -> str:
    model = lms.llm("qwq-32b")
    result = model.respond(message)
    return result


####
#### TODO: Create "Tools" for general purpose LLM to inteact with coding/empathy/math AIs 
####


#### TODO: Add "Search" Tool (via Tavily.us)
def tool_search(query:str) -> str:
    """ Search online using the given query. """
    api_key = os.getenv("TAVILY_KEY")
    tavily_client = TavilyClient(api_key=api_key)
    response = tavily_client.search(query)
    return response

#### TODO: Add "Text Messaging" tool to interact with other humans

def act_with_ai(message: str) -> str:
    model = lms.llm("qwq-32b")
    tools = [tool_multiply, tool_search]
    model.act(
        message,
        tools,
        on_message=print,
    )

def main():
    load_dotenv()
    print("Hello from ai-buddy!")
    result = act_with_ai("Search online to answer the following question, What is the name of the state bird of Utah?")
    print(result)


if __name__ == "__main__":
    main()
