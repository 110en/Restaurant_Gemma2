import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
load_dotenv()

class Llm:
    def __init__(self):
        self.llm = ChatGroq(
            model_name = "gemma2-9b-it",
            groq_api_key = os.getenv("GROQ_API_KEY"),
            temperature = 0.7
        )

    def name_gen(self, cuisine):
        prompt_name = PromptTemplate.from_template("I want to open a restaurant for {cuisine} food. Suggest A SINGLE fancy name for this. Remember, ONE name for a {cuisine} type restaurant. NO PREAMBLE")
        chain_name = prompt_name | self.llm
        name = chain_name.invoke(input = {"cuisine" : cuisine})
        return name.content
    
    def menu_gen(self, name, cuisine):
        prompt_menu = PromptTemplate.from_template("Suggest some menu items for {rest_name}, which is a {cuisine} type restaurant. Return it as a comma separated list.")
        chain_menu = prompt_menu | self.llm
        menu = chain_menu.invoke(input = {"rest_name" : name, "cuisine" : cuisine})
        return  menu.content
