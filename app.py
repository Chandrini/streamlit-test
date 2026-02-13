import streamlit as st
import pandas as pd

st.title("Hello world")

st.text("This is a web app to do stuff")

upload_file=st.file_uploader("Upload your files here")


if upload_file:
    df = pd.read_csv(upload_file)
    st.write(df.describe())

    st.header('Data Header')
    st.write(df.head())
