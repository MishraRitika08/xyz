import streamlit as st
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

@st.cache_resource(show_spinner="Reading and indexing your PDF...")
def process_pdf(upload):
    full_text = ""
    reader = PdfReader(upload)

    for page in reader.pages:
        text = page.extract_text() or ""
        # text = text.replace("\n", "")
        full_text += text.replace("\n", "")
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_text(full_text)

        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectordb = Chroma.from_texts(chunks, embedding=embeddings)
        # st.write(vectordb.similarity_search("Streaming platforms use AI", k=3))
        return vectordb
