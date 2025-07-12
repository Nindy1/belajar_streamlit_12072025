import streamlit as st

st.write("Hello, *World!* :sunglasses:")
import streamlit as st

st.title("Belajar Streamlit")

if st.button("Say hello"):
    st.write("Why hello there")
import streamlit as st

st.link_button("Go to gallery", "https://streamlit.io/gallery")
import streamlit as st
st.image("sunrise.jpg", caption="Sunrise by the mountains")

import time

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
