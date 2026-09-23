import streamlit as st
from utils.pdf_processor import process_pdf
from utils.llm import get_answer
st.set_page_config(
    page_title="ChatPDF",
    page_icon="📄",
    layout="wide"
)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = {}
if "vector_dbs" not in st.session_state:
    st.session_state.vector_dbs = {}
if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None

def uploadPdf(upload):
    pdf_name = upload.name
    st.session_state.current_pdf = pdf_name
    st.session_state.chat_history[pdf_name] = []
    new_pdf_vector = process_pdf(upload, pdf_name)
    st.session_state.vector_dbs[pdf_name] = new_pdf_vector

#app
with st.container(height = 600, border = True):
    st.title(":rainbow[📄 ChatPDF]")
    left, right = st.columns([1,3], gap = "large")

    with left:
        with st.container():
            st.subheader("Upload your pdf and ask questions about it")
            upload = st.file_uploader("Upload pdf here", type = ".pdf")

            if upload:
                
                if upload.name not in st.session_state.chat_history:
                    uploadPdf(upload)
                else:
                    st.session_state.current_pdf = upload.name
                st.session_state.current_pdf = upload.name
                st.success("PDF uploaded successfully!", icon="✅")
                st.write(f"name of the uploaded file: {upload.name}")

    with right:
        if upload:
            if st.session_state.current_pdf != None:
                curr = st.session_state.current_pdf
                st.write(f"💬Currently chatting with: {curr}")
                # display past messages
                st.write(st.session_state.current_pdf)
                st.write(st.session_state.chat_history.get(curr, []))
                messages = st.session_state.chat_history.get(curr, [])
                for msg in messages:
                    with st.chat_message(msg["role"]):
                        st.write(msg["content"])
                prompt = st.chat_input("Ask something about the PDF...")

                if prompt:
                    with st.chat_message("user"):
                        st.write(prompt)
                    vector_db = st.session_state.vector_dbs[curr] # get the db of this pdf
                    placeholder = st.empty()
                    placeholder.markdown(":shimmer[Generating answer...]")
                    response = get_answer(vector_db, prompt)
                    placeholder.empty()

                    if response:
                        with st.chat_message("assistant"):
                            st.write(response)
                        messages.append({"role": "user", "content": prompt})
                        messages.append({"role": "assistant", "content": response})
        else:
            st.write("Please upload a PDF to start chatting.")