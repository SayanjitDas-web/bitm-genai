import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

load_dotenv()
gemini_ai_api = os.getenv("GEMINI_AI_API")

llm = GoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = gemini_ai_api
)

query_prompt = PromptTemplate(
    template="Tell me about the topic {query}",
    input_variables=["query"]
)

summerize_prompt = PromptTemplate(
    template="{content} summerize the provided topic. return the response in a valid markdown format",
    input_variables=["content"]
)

chain = query_prompt | llm | summerize_prompt | llm

st.title("Topic summerizer..")

prompt = st.chat_input("enter topic you want to summerize..")

if prompt:
    user_message = st.chat_message("user")
    user_message.write(prompt)
    ai_message = st.chat_message("ai")
    ai_message.write("Ai is thinking..")
    result = chain.invoke({"query":prompt})
    ai_message.markdown(result)
