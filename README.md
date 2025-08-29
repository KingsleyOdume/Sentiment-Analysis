📊 Sentiment Analysis on Social Media Data

## 🚀 Project Overview
This project applies **Natural Language Processing (NLP)** techniques to analyze the sentiment of social media posts.  
Companies and recruiters want to know how customers feel about brands, products, or events — making sentiment analysis one of the most **practical data science skills**.

The project demonstrates:
- Data collection (Twitter API / Kaggle dataset)
- Text preprocessing (tokenization, stopword removal, lemmatization)
- Sentiment classification (positive, negative, neutral)
- Visualization of sentiment distribution
- Deployment on **Streamlit** for an interactive demo

---

## 🛠️ Tech Stack
- **Python 3.9+**
- [NLTK](https://www.nltk.org/) – Tokenization & stopword removal  
- [spaCy](https://spacy.io/) – Lemmatization  
- [Transformers](https://huggingface.co/transformers/) – Pre-trained BERT model for sentiment  
- [Matplotlib / Seaborn](https://matplotlib.org/) – Data visualization  
- [Streamlit](https://streamlit.io/) – Interactive web app  

---

## 📂 Project Structure

sentiment-analysis-social-media/
│── data/
│ └── sample_tweets.csv # Example dataset
│── notebooks/
│ └── sentiment_analysis.ipynb # Exploratory notebook
│── app/
│ └── streamlit_app.py # Streamlit app for live demo
│── requirements.txt # Dependencies
│── README.md # Documentation


---

## 📥 Dataset
- Option 1: Scrape live tweets using [Tweepy](https://www.tweepy.org/)  
- Option 2: Use a public dataset from [Kaggle Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140)  

For this repo, a **sample_tweets.csv** file is provided.

---

## ⚙️ Installation
Clone the repository:

git clone [https://github.com/yourusername/sentiment-analysis-social-media.git](https://github.com/KingsleyOdume/Sentiment-Analysis)
cd sentiment-analysis-social-media

Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt

▶️ Usage
1. Run Jupyter Notebook (exploration)
jupyter notebook notebooks/sentiment_analysis.ipynb

2. Run Streamlit App
streamlit run app/streamlit_app.py

streamlit run app/streamlit_app.py

Then open http://localhost:8501 in your browser.

🌐 Live Demo
👉 Deployed on Streamlit Cloud: [Streamlit App Link](https://sentiment-analysis-2cs89avcypamofcfcwbbzc.streamlit.app)

💡 Key Learnings
How to preprocess raw text data (cleaning, tokenizing, lemmatizing)
Applying Hugging Face Transformers for sentiment classification
Visualizing sentiment trends with Python
Deploying an interactive app with Streamlit

📌 Recruiter Note
This project demonstrates:
NLP expertise (text preprocessing + classification)
Business value (tracking customer sentiment)
Communication skills (dashboard + repo documentation)

👤 Author
Kingsley Odume
🌍 [Portfolio Website](https://kingsleyodume.online)
💻 [GitHub](https://github.com/KingsleyOdume)
🔗 [LinkedIn](https://linkedin.com/in/kingsleyodume)
