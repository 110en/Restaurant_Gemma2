import streamlit as st
from llm import Llm

st.title("Restaurant Name and Menu Generator")

cuisine = st.sidebar.text_input("Pick a Cuisine", value = "Iranian")
submit_button = st.sidebar.button("Enter")

if submit_button:
    restaurant = Llm.menu_gen(Llm.name_gen(cuisine))
    st.code(restaurant, langauge = "markdown")
