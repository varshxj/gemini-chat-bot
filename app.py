import streamlit as st
import google.generativeai as genai
from datetime import datetime

# Configure the API key directly (replace with your actual API key)
genai.configure(api_key="AIzaSyCTnCRfiWpNnQzxMepH4LUEGchDvTiS4-I")

# Streamlit app title
st.title("Gemini AI Chatbot")

# Introduction
st.write("Welcome! Ask me anything, and I'll do my best to provide an insightful response.")

# Input field for the user’s question
text = st.text_input("Enter your question")

# Option to reset the conversation history
if st.button("Reset Conversation"):
    chat = None
    st.session_state["chat_history"] = []

# Initialize or continue the chat session with history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
    chat = genai.GenerativeModel('gemini-pro').start_chat(history=st.session_state["chat_history"])
else:
    chat = genai.GenerativeModel('gemini-pro').start_chat(history=st.session_state["chat_history"])

# Submit the question and get a response
if st.button("Submit"):
    if text:
        st.session_state["chat_history"].append({"role": "user", "content": text})
        response = chat.send_message(text)
        st.session_state["chat_history"].append({"role": "assistant", "content": response.text})
        st.write(f"*You:* {text}")
        st.write(f"*Gemini:* {response.text}")
        st.write(f"*Response received at:* {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        st.write("Please enter a question first.")

# Display the full conversation history
if st.button("Show Conversation History"):
    st.write("### Conversation History")
    for entry in st.session_state["chat_history"]:
        role = "You" if entry["role"] == "user" else "Gemini"
        st.write(f"{role}:** {entry['content']}")