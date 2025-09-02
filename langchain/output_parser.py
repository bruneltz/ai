from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseOutputParser
import os

class AnswerParser(BaseOutputParser):
    def parse(self, text: str) -> str:
        "Parse the output text and return the answer."
        return text.strip().split("answer =")

api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key)

template = """You are a helpful assistant that solves math problems and explains the steps.
            output each step then the answer in the format: answer = <answer>.
            Make sure to output to answer in all lowercase and to have exactly one space and one equal sign."""
human_template = "{problem}"

chat_prompt = ChatPromptTemplate.from_messages([("system", template), ("human", human_template)])

chat_prompt_messages = chat_prompt.format_messages(problem="2x^2 + 3x - 5 = 0")

result = chat_model.invoke(chat_prompt_messages)
parsed = AnswerParser().parse(result.content)
steps, answer = parsed
print(answer)