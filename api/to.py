from together import Together
import os
from dotenv import load_dotenv

load_dotenv()

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

query = "What animals can I find near Peru?"

documents = [
  "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
  "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
  "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
  "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations.",
]

response = client.rerank.create(
  model="Salesforce/Llama-Rank-V1",
  query=query,
  documents=documents,
  top_n=2
)

for result in response.results:
    print(f"Document Index: {result.index}")
    print(f"Document: {documents[result.index]}")
    print(f"Relevance Score: {result.relevance_score}")