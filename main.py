import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')#, width=500)

with col2:
    st.title('Carl Jarvis')
    content = """There is a lot to say here   
    
    """
    st.info(content)