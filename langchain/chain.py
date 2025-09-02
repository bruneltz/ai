from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseOutputParser
import os

api_key = os.getenv("OPENAI_API_KEY")
chat_model = ChatOpenAI(openai_api_key=api_key)

class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str):
        "Parse the output text and return a list of items."
        return text.strip().split(", ")

template = "You are a helpful assistant that lists items in a comma-separated format. A user will provide a topic, and you will respond with a list of 5 items related to that topic, separated by commas. ONLY provide the list, do not include any additional text or punctuation."
human_template = "{topic}"

chat_prompt = ChatPromptTemplate.from_messages([("system", template), ("human", human_template)])

chain = chat_prompt | chat_model | CommaSeparatedListOutputParser()
result = chain.invoke("{topic: 'programming languages'}")
print(result)