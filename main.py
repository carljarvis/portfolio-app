import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')#, width=500)

with col2:
    st.title('Carl Jarvis')
    content = """There is a lot to say here   
    
    """
    st.info(content)


content2 = """Below you can find of the apps I have built in Python. Feel free to contact me!

"""

st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv('data.csv', sep=';')
with col3:
    # st.title('App Name')
    for index, row in df[:10].iterrows():
        # if index % 2== 0:
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        # if index % 2 == 1:
        st.header(row['title'])
