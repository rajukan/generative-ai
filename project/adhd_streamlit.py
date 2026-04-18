import streamlit as st
import json
from openai import OpenAI  # Updated import

# run via  streamlit run .\adhd_streamlit.py
# Load config
with open("./config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit UI
st.title("ADHD Chatbot Demo")

# Get list of available experiment types from config
available_experiment_types = list(config["system_prompts"].keys())

experiment_type = st.selectbox(
    "Select Experiment Type:",
    options=available_experiment_types,
    format_func=lambda x: x.replace("_", " ").title()
)

# Load selected model and system prompt
model_name = config["models"].get(experiment_type, "")
system_prompt = config["system_prompts"].get(experiment_type, "")

if not model_name or not system_prompt:
    st.error(f"Configuration for experiment type '{experiment_type}' is missing.")
    st.stop()

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": f"Hello! I'm here to discuss topics about ADHD based on the {experiment_type.replace('_', ' ')} experiment type. How can I help you today?"}
    ]

# Display chat messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything about ADHD..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get model response using the new OpenAI client
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=st.session_state.messages
            )
            assistant_response = response.choices[0].message.content
        except Exception as e:
            st.error(f"An error occurred: {e}")
            assistant_response = "Sorry, I encountered an error while processing your request."

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response)