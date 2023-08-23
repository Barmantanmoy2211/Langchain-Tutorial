import openai
import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain


# def practice():
# cities = [
#   "New York city",
#   "Los Angles",
#   "Chicago",
#   "Houston",
#   "Washington",
#   "Florida",
# ]
#   prompt = PromptTemplate.from_template("What is the capital of {place}?")
#   llm = OpenAI(temperature=0.3)
  
#   chain = LLMChain(llm=llm, prompt=prompt)
  
#   for city in cities:
#     output = chain.run(city)
#     print(output)


#LLM to get name of any commerce store
prompt = PromptTemplate.from_template("What is the name of the e commerce store that sells {product}?")
llm = OpenAI(temperature=0.3)
chain1 = LLMChain(llm=llm, prompt=prompt)

#LLM to get name of products from an e commerce name
prompt = PromptTemplate.from_template("What are the names of the products at {store}?")
llm = OpenAI(temperature=0.3)
chain2 = LLMChain(llm=llm, prompt=prompt)


#Create a overall chain from simple sequential chain
chain = SimpleSequentialChain(
  chains=[chain1, chain2], verbose=True
)

chain.run("candles")