import streamlit as st

#app
st.title("Welcome to llm-chat assistant")
st.header("Upload your pdf and ask questions about it")
upload = st.file_uploader("Upload your pdf", type = ".pdf")

if "messages" not in  st.session_state:
    st.session_state.messages = []

# display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if upload:
    st.write("Your pdf is uploaded successfully start chatting with your pdf")
    prompt = st.chat_input("Ask something about the PDF...", key = "chat_input")

    if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)
    
            response = "this is response that should be coming from llm after processing the pdf and user prompt"
    
            if response:
                st.session_state.messages.append({"role": "assistant", "content": response})
                with st.chat_message("assistant"):
                    st.write(response)
    
    








