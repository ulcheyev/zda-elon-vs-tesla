import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
import utils as ut
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
import re

df = ut.get_df('../data/tweets.csv')

def preprocess():
    df['text'].dropna(inplace=True)
    df.drop(columns=['username','favorites','replies','author_id', 'formatted_date','geo','id', 'permalink'], inplace=True)


def sentimentic_calc(text):
    sia = SentimentIntensityAnalyzer()
    val = sentiment_analyze(text)
    if val >= 0.05:
       return 1

    elif val <= - 0.05:
        return -1
    else:
        return 0

def sentiment_analyze(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)['compound']
def sentiment_calc_bolb(text):
    try:
        return TextBlob(text).sentiment
    except:
        return (0, 0)

def polarity_score(text):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)


def word_match_count(text, pattern):
    if text is None:
        return 0
    text = str(text)
    return len(re.findall(pattern, text))





