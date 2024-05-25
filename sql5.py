import openai
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import streamlit as st
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = "enter api_key_here"
llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], temperature=0.3)

st.title("paradedb SQL connect with Streamlit, langchain, and OpenAI")

command= st.text_input("enter the sql command")
prompt = PromptTemplate.from_template("{command} in sql command only give one suitable output")
# prompt.format(city="india")
# print(llm.predict(prompt))
chain = LLMChain(llm=llm, prompt=prompt)
output = chain.run(command)
print(output)
st.success(output)