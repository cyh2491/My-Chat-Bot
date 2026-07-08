# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()
# # load_dotenv(override = True)
# os.getenv("OPENAI_API_KEY")

# st.title("My Chat bot")

# if "messages" not in st.session_state:
#     st.session_state.messages = []
# prompt = st.chat_input("무엇을 도와드릴까요?")

# client = OpenAI()
# response = client.responses.create(
#     model="gpt-5.5",
#     input= prompt
# )

# if prompt:
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.session_state.messages.append({"role": "ai", "content": response.output_text})

#     for message in st.session_state.messages :
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
result = os.getenv("OPENAI_API_KEY")

print(result)

client = OpenAI()

st.title("My Chatbot")

if "messages" not in st.session_state : 
    st.session_state.messages = []

prompt = st.chat_input("무엇이든 물어보세요")

if prompt:
    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    st.session_state.messages.append({'role' : 'user', 'content' : prompt})
    st.session_state.messages.append({'role' : 'ai', 'content' : response.output_text})

    for message in st.session_state.messages : 
        with st.chat_message(message['role']) :
            st.write(message['content'])
            