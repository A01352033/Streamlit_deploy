import streamlit as st

# Web page to tell my couple I love her 
st.set_page_config(page_title="Anaí pendeja", page_icon="❤️")
st.title("Anaí pendeja")
st.write("Tkm")

# Make a heart with ascii art
st.write("""
```
    .-.-.  .-.-.
     (     )(     )
    `-.-'  `-.-'
    """)
# Add a button to go to the next page
if st.button("Next"):
    st.write("Next page")
    st.balloons()
# Add a button to go to the previous page   
if st.button("Previous"):
    st.write("Previous page")
    st.balloons()
# Add a button to go to the home page
if st.button("Home"):
    st.write("Home page")
    st.balloons()
# Add a button to go to the contact page
if st.button("Contact"):
    st.write("Contact page")
    st.balloons()
# Add a button to go to the about page
if st.button("About"):
    st.write("About page")
    st.balloons()
# Add a button to go to the help page
if st.button("Help"):
    st.write("Help page")
    st.balloons()
# Add a button to go to the settings page
if st.button("Settings"):
    st.write("Settings page")
    st.balloons()
# Add a button to go to the feedback page
if st.button("Feedback"):
    st.write("Feedback page")
    st.balloons()
# Add a button to go to the support page
if st.button("Support"):
    st.write("Support page")
    st.balloons()
    