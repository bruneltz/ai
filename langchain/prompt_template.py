from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os

api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key)

template = "You are a assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([("system", template), ("human", human_template)])

chat_prompt_messages = chat_prompt.format_messages(
    input_language="English", output_language="Portuguese", text="I love programming."
)

result = chat_model.invoke(chat_prompt_messages)
print(result.content)