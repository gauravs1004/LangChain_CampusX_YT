from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-5.6-terra")

result = llm.invoke("What is the capital of France?")

print(result.content)
