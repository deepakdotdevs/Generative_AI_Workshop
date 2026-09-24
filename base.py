import streamlit as st
import requests
import json

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖", layout="centered")

st.title("Groq Chatbot")

API_URL = "https://api.groq.com/openai/v1/chat/completions"

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Groq API Key", type="password", value="YOUR_API_KEY")
    model_name = st.selectbox("Model", ["openai/gpt-oss-20b", "llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768"])
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

def get_groq_response(messages, api_key, model):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": messages
    }
    
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_data = response.json()
            return response_data['choices'][0]['message']['content']
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message..."):
    if not api_key:
        st.error("Please provide a valid Groq API Key.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response_text = get_groq_response(st.session_state.messages, api_key, model_name)
                st.markdown(response_text)
        
                st.session_state.messages.append({"role": "assistant", "content": response_text})