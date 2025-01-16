import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model_name = "gemma2-9b-it",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature = 0.7
)

print(llm.invoke("I want to open a restaurant for Iranian food. Suggest a fancy name for this.").content)