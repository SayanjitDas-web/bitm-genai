import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

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

st.title("Chatbot for your daily quetions!")

result = ""
prompt = st.chat_input("tell me the query..")

if prompt:
    user_message = st.chat_message("user")
    user_message.write(prompt)
    ai_message = st.chat_message("ai")
    with st.spinner("Ai is thinking...", show_time=True):
        result = chain.invoke({"query":prompt})
        ai_message.markdown(result)
    st.toast("happy to help you!", icon="😍")
    if st.button("summerize in 100 words"):
        if result:
            result = llm.invoke(f"{result} summerize this in 100 words and return the response in a valid markdown format. ")
            ai_message_two = st.chat_message("ai")
            ai_message_two.markdown(result)