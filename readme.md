ChatPDF
A RAG-based PDF question-answering application built with Streamlit.
Upload a PDF and ask questions based on its content.

## Features

- Upload and process PDF documents
- Extract text from PDFs
- Split extracted tex into chunks of size 1000
- Generate embeddings using Hugging Face
- Store embeddings in ChromaDB
- Retrieve relevant content using similarity search
- Generate answers using Groq LLM
- Chat-based interface using Streamlit

## Tech Stack

- Python
- Streamlit
- LangChain
- Hugging Face Embeddings
- ChromaDB
- Groq API
- PyPDF

## How It Works

PDF -> Text Extraction -> Text Chunking -> Hugging Face Embeddings -> ChromaDB -> Similarity Search -> Relevant Context -> Groq LLM -> Answer
