from langchain_openai import ChatOpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key)

result = chat_model.invoke("Hi")
print(result.content)