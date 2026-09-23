import streamlit as st
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import re
@st.cache_resource(show_spinner="Reading and indexing your PDF...")
def process_pdf(upload, name):
    full_text = ""
    reader = PdfReader(upload)
    name = re.sub(r"[^0-9a-zA-Z]", "_", name)
    for page in reader.pages:
        text = page.extract_text() or ""
        full_text += text.replace("\n", "")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(full_text)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_texts(chunks, embedding=embeddings, collection_name=f"pdf_{name}")

    return vectordb
