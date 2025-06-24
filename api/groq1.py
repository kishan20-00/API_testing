import os
import json
from groq import Groq
from pydantic import BaseModel, Field, ValidationError # pip install pydantic
from typing import List
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is the current weather in Tokyo?",
        }
    ],
    # Change model to compound-beta to use agentic tooling
    # model: "llama-3.3-70b-versatile",
    model="compound-beta",
)

print(completion.choices[0].message.content)