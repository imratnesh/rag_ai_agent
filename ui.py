import streamlit as st
from rag import chat_with_rag

st.title("Local AI Agent with RAG")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

query = st.chat_input("Ask something...")
if query:
    st.chat_message("user").write(query)
    response = chat_with_rag(query)
    st.chat_message("assistant").write(response)

    st.session_state["messages"].append({"role": "user", "content": query})
    st.session_state["messages"].append({"role": "assistant", 
                                         "content": response})
