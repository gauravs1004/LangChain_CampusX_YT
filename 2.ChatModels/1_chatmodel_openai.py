from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model_name="gpt-5.6-terra", temperature=0.9, max_completion_tokens=50
)

result = model.invoke("Write the 5 lines poem about the game of cricket?")
print(result.content)
