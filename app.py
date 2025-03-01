import streamlit as st
import pandas as pd
import re
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Title
st.title("📧 Spam Email Detection App")

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Data Preprocessing", "Visualization", "Spam Detection"])

# Home Page
if page == "Home":
    st.header("🏠 Welcome to the Streamlit Basics Assignment")

    st.subheader("What is Streamlit?")
    st.markdown("""
    Streamlit is an open-source Python framework used to build interactive web applications for data science and machine learning.
    It allows you to create apps with minimal code and provides built-in widgets for interactivity.
    """)

    # User Interaction Widgets
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

# File Uploader
uploaded_file = st.sidebar.file_uploader("📂 Upload a CSV file of emails:", type=["csv"], key="file_uploader_1")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # Load CSV into DataFrame
    st.sidebar.success("✅ Dataset Loaded Successfully!")

    # Debugging: Display available columns
    st.sidebar.write("📌 Available Columns:", df.columns.tolist())

    # Column Name Detection
    text_column = None
    if "Message" in df.columns:
        text_column = "Message"
    elif "email" in df.columns:
        text_column = "email"
    elif "text" in df.columns:
        text_column = "text"
    else:
        st.sidebar.error("❌ No valid text column found! Expected 'Message', 'email', or 'text'.")
        st.stop()

    # Spam Category Detection
    label_column = None
    if "Category" in df.columns:
        label_column = "Category"
    elif "label" in df.columns:
        label_column = "label"
    else:
        st.sidebar.error("❌ No valid category column found! Expected 'Category' or 'label'.")
        st.stop()

    # Data Preprocessing Page
    if page == "Data Preprocessing":
        st.header("🛠 Data Preprocessing")

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

        # Apply Preprocessing
        df["Processed_Text"] = df[text_column].apply(preprocess_text)
        st.write("✅ Text Preprocessing Completed!")

        # Show Processed Data
        st.dataframe(df[[text_column, "Processed_Text"]])

    # Visualization Page
    elif page == "Visualization":
        st.header("📊 Spam vs. Ham Email Distribution")

        # Spam vs. Ham Bar Chart
        spam_counts = df[label_column].value_counts()

        fig, ax = plt.subplots()
        ax.bar(spam_counts.index, spam_counts.values, color=['green', 'red'])
        ax.set_xlabel("Email Type")
        ax.set_ylabel("Count")
        ax.set_title("Spam vs Ham Email Distribution")

        st.pyplot(fig)

elif page == "Spam Detection":
    st.header("🚀 Spam Detection with WordCloud")

    from wordcloud import WordCloud

    # Ensure Processed_Text Exists
    if "Processed_Text" not in df.columns:
        st.warning("⚠️ Preprocessing not applied! Running it now...")
        df["Processed_Text"] = df[text_column].apply(preprocess_text)
        st.success("✅ Preprocessing Applied Successfully!")

    # Spam WordCloud
    spam_words = " ".join(df[df[label_column] == "spam"]["Processed_Text"])
    spam_wordcloud = WordCloud(width=600, height=400, background_color="black").generate(spam_words)

    st.subheader("🛑 Spam Emails Word Cloud")
    st.image(spam_wordcloud.to_array())

    # Ham WordCloud
    ham_words = " ".join(df[df[label_column] == "ham"]["Processed_Text"])
    ham_wordcloud = WordCloud(width=600, height=400, background_color="black").generate(ham_words)

    st.subheader("✅ Ham Emails Word Cloud")
    st.image(ham_wordcloud.to_array())

