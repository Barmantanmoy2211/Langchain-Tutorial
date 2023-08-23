import openai
# import langchain
import os

from langchain.llms import OpenAI

llm = OpenAI(temperature=0.3)
print(llm.predict("WHat is the capital of India?"))
