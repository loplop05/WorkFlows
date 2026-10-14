
from  ollama import chat

def get_price(product: str) -> str:
    """Return the price of a product."""
    prices = {
        "Laptop A": 500,
        "Laptop B": 750,
    }
    return str(prices.get(product, "Not found"))

messages = [
    {
        "role": "user",
        "content": "What is the price of Laptop B?"
    }
]

for step in range(10):
    response = chat(
        model="qwen2.5:3b",
        messages=messages,
        tools=[get_price],
    )

    messages.append(response.message)

    if not response.message.tool_calls:
        print(response.message.content)
        break

    for call in response.message.tool_calls:
        if call.function.name != "get_price":
            raise ValueError("Unknown tool")

        result = get_price(**call.function.arguments)

        messages.append({
            "role": "tool",
            "tool_name": call.function.name,
            "content": result,
        })
else:
    print("Stopped: maximum steps reached")
