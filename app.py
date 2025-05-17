import os
import torch
import streamlit as st
from rag import add_resume_to_db, chat_with_rag
torch.classes.__path__ = [os.path.join(torch.__path__[0], torch.classes.__file__)] 

# or simply:
torch.classes.__path__ = []


st.title("📄 Resume AI Agent with RAG")

# File Upload Section
uploaded_file = st.file_uploader("Upload a Resume (PDF)", type=["pdf"])

if uploaded_file:
    file_path = f"./resumes/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    message = add_resume_to_db(file_path)
    st.success(message)

# Chat Interface
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

query = st.chat_input("Ask something about a candidate...")
if query:
    st.chat_message("user").write(query)
    response = chat_with_rag(query)
    st.chat_message("assistant").write(response)

    st.session_state["messages"].append({"role": "user", "content": query})
    st.session_state["messages"].append({"role": "assistant", "content": response})
