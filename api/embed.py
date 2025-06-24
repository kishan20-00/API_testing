import openai

client = openai.OpenAI(
    base_url="https://api.sambanova.ai/v1",
    api_key="b70a6f92-ce7b-4f3e-a0e7-ec1cd95cd6f9",
)

response = client.embeddings.create(
    model="E5-Mistral-7B-Instruct",
    input="The quick brown fox jumps over the lazy dog"
)

print(response)