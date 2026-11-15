from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = ["Delhi is capital of India",
             "Mumbai is the financial capital of India",
             "Kolkata is the cultural capital of India"]

results = embedding.embed_documents(documents)

print(str(results))
