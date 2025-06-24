from openai import OpenAI
client = OpenAI(
    base_url="https://api.sambanova.ai/v1", 
    api_key="b70a6f92-ce7b-4f3e-a0e7-ec1cd95cd6f9"
)
completion = client.chat.completions.create(
    model="Meta-Llama-3.1-8B-Instruct",
    messages = [
        {"role": "user", "content": "Hi! My name is Peter and I am 31 years old. What is 1+1?"},
        {"role": "assistant", "content": "Nice to meet you, Peter. 1 + 1 is equal to 2"},
        {"role": "user", "content": "What is my age?"}
    ],
    stream = True
)
for chunk in completion:
  print(chunk.choices[0].delta.content, end="")