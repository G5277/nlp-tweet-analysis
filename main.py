import re
import nltk
import random
import string
import matplotlib.pyplot as plt 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import twitter_samples
from nltk.tokenize import TweetTokenizer

# downloads
nltk.download('twitter_samples')
nltk.download('stopwords')

def biclass_plot(class_a, class_b):

    fig = plt.figure(figsize = (5,5))
    labels = 'Positive', 'Negative'
    size = [len(pos_tweets), len(neg_tweets)]
    plt.pie(size,labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 70)
    plt.axis('equal')
    plt.show()

def classify(dataset):
    pos_tweets = dataset.strings('positive_tweets.json')
    neg_tweets = dataset.strings('negative_tweets.json')

    # biclass_plot(pos_tweets, neg_tweets)

    return pos_tweets,neg_tweets

def preprocess(class_i):
    tweet = class_i[random.randint(0,len(class_i))]
    # remove hyperlinks
    tweet = re.sub(r'https?://[^\s\n\r]+', '', tweet)
    # remove hashtags
    tweet = re.sub(r'#','', tweet)

    return tweet


def tokenize_string(string_i):
    tokenizer = TweetTokenizer(preserve_case = False, strip_handles = True, reduce_len = True)
    return tokenizer.tokenize(string_i)

def remove_stopwords(list_i):
    stopwords_english = stopwords.words('english')
    clean = []
    for word in list_i:
        if ( word not in stopwords_english and word not in string.punctuation):
            clean.append(word)
    return clean

def stemming(list_i):
    stemmer = PorterStemmer()
    stem = []
    for word in list_i:
        stem_word = stemmer.stem(word)
        stem.append(stem_word)

    return stem

# Classify
pos_tweets,neg_tweets = classify(twitter_samples)

# Preprocess
tweet = preprocess(pos_tweets)


# Tokenize
tweet_tokens = tokenize_string(tweet)

# Remove Stopwords
tweet_clean = remove_stopwords(tweet_tokens)

# Stemming
tweets_stem = stemming(tweet_clean)

# Instead of all this manual processing we can use
# process_tweet

from utils import process_tweet

stem_tweets = process_tweet(tweet)

# Result Match
print(stem_tweets, "   ", tweets_stem)