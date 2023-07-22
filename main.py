import streamlit as st
import pandas as pd
import plotly.express as px
import base64

st.set_page_config(layout="wide")

st.title("Connectiv")
st.subheader("A Marketplace to find teammates for competitions")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Darren Weng")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("Gabe Weng")
   st.text("Gabe is so cool")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("Julian Weng")
   st.image("https://static.streamlit.io/examples/owl.jpg")
