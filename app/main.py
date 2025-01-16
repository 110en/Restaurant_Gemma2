import streamlit as st
from llm import Llm

st.title("Restaurant Name & Menu Gen")

cuisine = st.sidebar.text_input("Pick a Cuisine", value = "Iranian")
submit_button = st.sidebar.button("Enter")
ai = Llm()
if submit_button:
    name = ai.name_gen(cuisine)
    menu = ai.menu_gen(name, cuisine)
    restaurant = name + "\n" + menu
    st.code(restaurant, language = "markdown")
