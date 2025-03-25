import lmstudio as lms
from dotenv import load_dotenv
from tools import tool_belt

def chat_with_ai(message: str) -> str:
    model = lms.llm("qwq-32b")
    result = model.respond(message)
    return result

def print_fragment(fragment, round_index=0):
    print(fragment.content, end="", flush=True)

def act_with_ai(message: str) -> str:
    model = lms.llm("qwq-32b")
    chat = lms.Chat("You are a tool using AI focused on finding a solution to the user's problem. Make sure to think step by step")
    chat.add_user_message(message)
    
    return model.act(
        chat,
        tools=tool_belt.tools,
        on_message=chat.append,
        on_prediction_fragment=print_fragment,
    )

def main():
    load_dotenv()
    print("Hello from ai-buddy!")
    result = act_with_ai("What is the weather in Warrington, PA?")
    print(result)


if __name__ == "__main__":
    main()
