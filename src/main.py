import streamlit as st
from decouple import config
import openai

response = False
prompt_tokens = 0
completion_tokes = 0
total_tokens_used = 0
cost_of_response = 0

API_KEY = config('OPENAI_API_KEY')
openai.api_key = API_KEY


def make_request(question_input: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"{question_input}"},
        ]
    )
    return response


st.header("Streamlit + OpenAI ChatGPT API")

st.markdown("""---""")

question_input = st.text_input("Enter question")
rerun_button = st.button("Rerun")

st.markdown("""---""")

if question_input:
    response = make_request(question_input)
else:
    pass

if rerun_button:
    response = make_request(question_input)
else:
    pass

if response:
    st.write("Response:")
    st.write(response["choices"][0]["message"]["content"])

    prompt_tokens = response["usage"]["prompt_tokens"]
    completion_tokes = response["usage"]["completion_tokens"]
    total_tokens_used = response["usage"]["total_tokens"]

    cost_of_response = total_tokens_used * 0.000002
else:
    pass


with st.sidebar:
    st.title("Usage Stats:")
    st.markdown("""---""")
    st.write("Promt tokens used :", prompt_tokens)
    st.write("Completion tokens used :", completion_tokes)
    st.write("Total tokens used :", total_tokens_used)
    st.write("Total cost of request: ${:.8f}".format(cost_of_response))
