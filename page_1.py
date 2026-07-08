import streamlit as st




st.title("동물 사진")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

tab1, tab2, tab3, tab4 = st.tabs(["harajuku", "sizuoka", "azabu1", "azabu2"])


with tab1:
    st.header("harajuku")
    st.image("harajuku1.jpg", width=800)
    # st.image("harajuku1.jpg", use_container_width=True)
with tab2:
    st.header("sizuoka")
    st.image("sizuoka.jpg", width=800)
with tab3:
    st.header("azabu1")
    st.image("azabu1.jpg", width=800)
with tab4:
    st.header("azabu2")
    st.image("azabu2.jpg", width=800)