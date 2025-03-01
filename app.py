

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

import streamlit as st
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Streamlit file uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # Read CSV
    st.write("✅ Dataset Loaded Successfully!")

    # Display column names
    st.write("🔹 Available columns:", df.columns.tolist())

    # Check if the 'Message' column exists
    if "Message" in df.columns:
        # Text Preprocessing Function
        def preprocess_text(text):
            text = str(text).lower()  # Convert to lowercase
            text = re.sub(r'\d+', '', text)  # Remove numbers
            text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
            words = word_tokenize(text)  # Tokenization
            words = [word for word in words if word not in stopwords.words('english')]  # Remove stopwords
            stemmer = PorterStemmer()
            words = [stemmer.stem(word) for word in words]  # Stemming
            return " ".join(words)

        # Apply preprocessing
        df["Processed_Text"] = df["Message"].apply(preprocess_text)
        st.dataframe(df[["Message", "Processed_Text"]])  # Show processed data

    else:
        st.error("❌ Column 'Message' not found in the uploaded CSV. Please check your file.")

import matplotlib.pyplot as plt

if uploaded_file is not None:
    # Fix: Use "Category" instead of "label"
    spam_counts = df["Category"].value_counts()

    fig, ax = plt.subplots()
    ax.bar(spam_counts.index, spam_counts.values)
    ax.set_xlabel("Email Type")
    ax.set_ylabel("Count")
    ax.set_title("Spam vs Ham Email Distribution")

    st.pyplot(fig)
