import openai
import cmath
import random
import json

# Define the OpenAI client
client = openai.OpenAI(
    base_url="https://api.sambanova.ai/v1", 
    api_key="b70a6f92-ce7b-4f3e-a0e7-ec1cd95cd6f9"
)

MODEL = 'Meta-Llama-3.3-70B-Instruct'

def get_weather(city: str) -> dict: 
    """
    Fake weather lookup: returns a random temperature between 20°C and 50°C.
    """
    temp = random.randint(20, 50)
    return {
        "city": city,
        "temperature_celsius": temp
    }


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of an location, the user shoud supply a location first",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["city"]
            },
        }
    },
]

messages = [{"role": "user", "content": "What's the weather like in Paris today?"}]


completion = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    tools=tools
)

print(completion)


tool_call = completion.choices[0].message.tool_calls[0]
args = json.loads(tool_call.function.arguments)

result = get_weather(args["city"])


messages.append(completion.choices[0].message)  # append model's function call message
messages.append({                               # append result message
    "role": "tool",
    "tool_call_id": tool_call.id,
    "content": str(result)
})

completion_2 = client.chat.completions.create(
    model=MODEL,
    messages=messages,
 
)
print(completion_2.choices[0].message.content)