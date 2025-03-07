import streamlit as st
from functions import is_ready_to_kaburajadulu

st.title("Kabur Aja Dulu???")

age = st.number_input("Enter your age", min_value=1, max_value=100, step=1)
can_speak_english = st.selectbox("Can you speak English?", options=["Yes", "No"])
having_dev_skills = st.selectbox("Do you have dev skills?", options=["Yes", "No"])

if st.button("Check"):
    st.success(is_ready_to_kaburajadulu(age, can_speak_english, having_dev_skills))
