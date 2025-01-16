import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(temperature = 0.75)
print(llm("I want to open a restaurant for Iranian food. Suggest a fancy name for this."))