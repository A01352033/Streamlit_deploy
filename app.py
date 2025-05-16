import streamlit as st

st.title("Hello, world!")
st.write("This is a simple Streamlit app.")
st.text_input("Enter your name:", "")
st.text_area("Enter your message:", "")
st.button("Submit")

# Add a sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is a sidebar.")
st.sidebar.text_input("Enter your age:", "")
st.sidebar.text_area("Enter your address:", "")
st.sidebar.button("Submit to Sidebar")
st.sidebar.write("This is a sidebar button.")
st.sidebar.write("This is a sidebar text.")
st.sidebar.write("This is a sidebar text.")