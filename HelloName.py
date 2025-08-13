# save this file as app.py
import streamlit as st

st.title("Simple Greeting App")

# Get the user's name
name = st.text_input("Enter your name:")

# When the user types something, display the greeting
if name:
    st.write(f"Hello there, {name}!")
