

import streamlit as st

# Title and Header
st.title("Spam Email Detection App")
st.header("Welcome to the Streamlit Basics Assignment")

# Subheader and Markdown
st.subheader("What is Streamlit?")
st.markdown("""
Streamlit is an open-source Python framework used to build interactive web applications for data science and machine learning.
It allows you to create apps with minimal code and provides built-in widgets for interactivity.
""")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Welcome, {name}!")

language = st.selectbox("Choose your favorite programming language:", ["Python", "Java", "C++", "JavaScript"])
st.write(f"You selected: {language}")

number = st.slider("Select a number:", 1, 100)
st.write(f"Selected number: {number}")


if st.checkbox("Show message"):
    st.write("This is a secret message!")


level = st.radio("Select your skill level:", ["Beginner", "Intermediate", "Advanced"])
st.write(f"You are at the {level} level.")


uploaded_file = st.file_uploader("Upload a CSV file of emails:", type=["csv"])
if uploaded_file:
    st.write("File uploaded successfully!")

import pandas as pd

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Data Preprocessing", "Visualization", "Spam Detection"])


