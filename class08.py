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
    template="Tell me about the person {query}. only reaturn the response in a valid markdown format.",
    input_variables=["query"]
)

chain = query_prompt | llm

result = chain.invoke({"query":"srk"})
# result = llm.invoke("tell me about srk.")

print(result)