import streamlit as st
from transformers.pipelines import pipeline

print("import succed")

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")  # 👈 Load the model

model = load_model()  # 👈 Load the model once
query = st.text_input("Your query", value="I love Streamlit! 🎈")
if query:
    result = model(query)[0]  # 👈 Classify the query text
    st.write(result)