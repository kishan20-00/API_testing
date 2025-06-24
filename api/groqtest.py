from openai import OpenAI
client = OpenAI(
    base_url="https://api.groq.com/openai/v1", 
    api_key="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"
)
completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages = [  
        {"role": "system", "content": "Answer the question in a couple sentences."},
        {"role": "user", "content": "Share a happy story with me"}
    ]
)
print(completion)