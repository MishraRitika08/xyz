import streamlit as st
from groq import Groq

def get_answer(vectordb, question):
    docs = vectordb.similarity_search(question, k=4)
    context = "\n\n".join(d.page_content for d in docs)

    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": (
                "Answer ONLY using the provided context from the PDF. "
                "If the answer isn't in the context, say you don't know based on this document."
            )},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        ]
    )
    return completion.choices[0].message.content