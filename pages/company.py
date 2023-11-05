import streamlit as st
import pandas as pd

# Add a header and some other text
st.header("The Best Company")
st.write("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
officia deserunt mollit anim id est laborum.""")
st.subheader("Our Team")

# Prepare the columns
col1, col2, col3 = st.columns(3)

df = pd.read_csv('./pages/company/data.csv')


#print()
with col1:
    for index, row in df[:4].iterrows():
        # index % 3 == 0:
        st.subheader('{} {}'.format(row['first name'].title(), row['last name'].title()))
        st.write(row['role'])
        st.image('./pages/company/images/{}'.format(row['image']))

with col2:
    for index, row in df[4:8].iterrows():
        #if index % 3 == 1:
        st.subheader('{} {}'.format(row['first name'].title(), row['last name'].title()))
        st.write(row['role'])
        st.image('./pages/company/images/{}'.format(row['image']))

with col3:
    for index, row in df[8:12].iterrows():
        #if index % 3 == 2:
        st.subheader('{} {}'.format(row['first name'].title(), row['last name'].title()))
        st.write(row['role'])
        st.image('./pages/company/images/{}'.format(row['image']))