import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

file_path = "job.jsonl"
response = client.files.create(file=open(file_path, "rb"), purpose="batch")

print(response)