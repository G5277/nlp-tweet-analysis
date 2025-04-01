import nltk
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
import numpy as np 

nltk.download('twitter_samples')
nltk.download('stopwords')

from utils import process_tweet, build_freqs

all_pos = twitter_samples.strings('positive_tweets.json')
all_neg = twitter_samples.strings('negative_tweets.json')

tweets = all_pos + all_neg
# print(f"Number of tweets : {len(tweets)}")
