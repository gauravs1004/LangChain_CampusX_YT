from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    max_tokens=100,
)

result = llm.invoke("Write a 5 lines poem about the game of cricket?")

print(result.content)