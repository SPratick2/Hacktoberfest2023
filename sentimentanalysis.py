import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (if not already downloaded)
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    if compound_score <= 0.05 and compound_score >= -0.05:
        sentiment = "Neutral"
    elif compound_score >= 0.05:
        sentiment = "Positive"
    else: 
        sentiment = "Negative"
    return sentiment,sentiment_scores

sample_text = "I love this product! It's amazing."
sentiment, scores = analyze_sentiment(sample_text)
print("Sentiment:", sentiment)
print("Sentiment Scores:", scores)
