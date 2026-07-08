import streamlit as st
import numpy as np

st.title("My Chat bot")

# prompt = st.chat_input("무엇이든 물어보세요")
# if prompt:
#     st.write(prompt)

#     with st.chat_message("user"):
#         st.write("Hello 👋")
#         # st.line_chart(np.random.randn(30, 3))
#     with st.chat_message("ai"): # ai 또는 assisatant
#         st.write('반갑습니다.')

# 채팅을 칠때마다 아래 코드를 재실행한다.
# 이를 해결 하기 위해 아래 코드가 요구된다.


# 세션에 messages 저장공간 만들기 (처음 실행 시 1회만 생성)
if "messages" not in st.session_state:
    st.session_state.messages = []
prompt = st.chat_input("무엇을 도와드릴까요?")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "ai", "content": "반갑습니다."})

    for message in st.session_state.messages :
        with st.chat_message(message["role"]):
            st.markdown(message["content"])