import streamlit as st

from models.oss_model import chat_with_oss
from models.frontier_model import chat_with_gemini

st.title("AI Assistant Comparison")
if st.button("Clear Chat"):
    st.session_state.messages = []
model_choice = st.selectbox(
    "Choose Assistant",
    ["OSS Assistant", "Gemini Assistant"]
)


if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your message")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    st.chat_message("user").write(user_input)

    if model_choice == "OSS Assistant":

        response = chat_with_oss(
            st.session_state.messages
        )

    else:

        response = chat_with_gemini(
            st.session_state.messages
        )

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.chat_message("assistant").write(response)