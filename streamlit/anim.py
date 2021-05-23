
import streamlit as st



st.title("Hello World")
st.write("""
         
         #Text Markup Language
         Random text
         another random text
         """)

length = st.slider(max_value=3.0,min_value=0.0,value=0.0,step=0.1,label="temperature")

st.write(length)