import streamlit as st
from llm import Llm

st.title("Restaurant Name and Menu Generator")

cuisine = st.sidebar.text_input("Pick a Cuisine", value = "Iranian")
submit_button = st.sidebar.button("Enter")

if submit_button:
    name = Llm.name_gen(cuisine)
    menu = Llm.menu_gen(name, cuisine)
    restaurant = name + "\n" + menu
    st.code(restaurant, langauge = "markdown")
