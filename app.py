import streamlit as st
from openai import OpenAI
import os

client = OpenAI()

# Set up the Streamlit app
st.title("Where Was (A)I?")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is your question?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call OpenAI API to get response
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(completion.choices[0].message)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": completion.choices[0].message})