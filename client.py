import requests
import streamlit as st

## Streamlit app
st.title("LLM Application Using LCEL")

# Language selection
select_language = st.selectbox("Select Language to translate:", ("English", "Hindi", "French", "Arabic", "Chinese"))

# Text input
input_text = st.text_input(f"Enter the text you want to convert to {select_language}")

# Function to call LangChain server
def get_groq_response(input_text):
    json_body = {
        "input": {
            "language": select_language,
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }
    try:
        response = requests.post("http://localhost:8000/chain/invoke", json=json_body)
        response.raise_for_status()
        translated_text = response.json().get("output", "No output found")
        return translated_text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Display translated result
if input_text:
    translated_output = get_groq_response(input_text)
    st.subheader("Translated Text:")
    st.write(translated_output)