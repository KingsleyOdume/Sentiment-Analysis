import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

# Load pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

st.title("📊 Sentiment Analysis on Social Media Data")
st.write("Analyze sentiment (positive, negative, neutral) of social media posts in real-time.")

# User Input
user_input = st.text_area("Enter a tweet or text:")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        result = sentiment_pipeline(user_input)[0]
        st.write(f"**Label:** {result['label']}")
        st.write(f"**Confidence:** {result['score']:.2f}")
    else:
        st.warning("Please enter some text.")

# Load sample data
if st.checkbox("Show sentiment distribution for sample dataset"):
    df = pd.read_csv("data/sample_tweets.csv")
    df['sentiment'] = df['text'].apply(lambda x: sentiment_pipeline(x[:512])[0]['label'])
    
    sentiment_counts = df['sentiment'].value_counts()
    
    fig, ax = plt.subplots()
    sentiment_counts.plot(kind='bar', ax=ax)
    ax.set_title("Sentiment Distribution")
    st.pyplot(fig)
