from transformers import AutoModelForCausalLM, AutoTokenizer
import lmstudio as lms

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

def act_with_ai(message: str) -> str:
    model = lms.llm("qwq-32b")
    tools = [tool_multiply]
    model.act(
        message,
        tools,
        on_message=print,
    )

def main():
    print("Hello from ai-buddy!")
    result = act_with_ai("What is the result of 1200 multipled by 333?")
    print(result)


if __name__ == "__main__":
    main()
