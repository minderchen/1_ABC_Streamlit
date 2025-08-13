import os
import streamlit as st
from openai import OpenAI
# from dotenv import load_dotenv  # optional for local dev
# load_dotenv()  # ok to keep for local .env, ignored on Streamlit Cloud

st.title("Hello, GenAI!")
st.write("This is your first Streamlit app.")

# Get the key: prefer Streamlit secrets, fallback to environment variable for local dev
api_key = st.secrets.get("OPENAI_API_KEY") 
# or os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Missing OPENAI_API_KEY. Add it in Streamlit → App → Settings → Secrets.")
    st.stop()

# Initialize OpenAI client (either pass the key or export it to env)
client = OpenAI(api_key=api_key)
# Alternatively:
# os.environ["OPENAI_API_KEY"] = api_key
# client = OpenAI()

prompt = "Explain generative AI in one sentence."
response = client.responses.create(
    model="gpt-4o",
    input=[{"role": "user", "content": prompt}],
    temperature=0.7,
    max_output_tokens=100,
)

# Easiest way to print the text
st.write(response.output_text)
