import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains import sequential

load_dotenv()

llm = ChatGroq(
    model_name = "gemma2-9b-it",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature = 0.7
)

#print(llm.invoke("I want to open a restaurant for Iranian food. Suggest a fancy name for this.").content)
prompt_name = PromptTemplate.from_template("I want to open a restaurant for {cuisine} food. Suggest A SINGLE fancy name for this. Remember, ONE name for a {cuisine} type restaurant")
chain_name = prompt_name | llm
name = chain_name.invoke(input = {"cuisine" : input("Cuisine Wanted (Press Enter When Finished): ")})
print(name.content)

prompt_menu = PromptTemplate.from_template("Suggest some menu items for {rest_name}. Return it as a comma separated list.")
chain_menu = prompt_menu | llm
menu = chain_menu.invoke(input = {"rest_name" : name.content})
print(menu.content)


