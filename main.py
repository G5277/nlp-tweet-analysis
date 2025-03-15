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

# pos and neg tweets
pos_tweets = twitter_samples.strings('positive_tweets.json')
neg_tweets = twitter_samples.strings('negative_tweets.json')
print(f'Pos Tweets : {pos_tweets} | type : {type(pos_tweets)}')
print(f'Neg Tweets : {neg_tweets} | type : {type(neg_tweets)}')

# plotting information 

# figure
fig = plt.figure(figsize = (5,5))
# labels
labels = 'Positive', 'Negative'
# size
size = [len(pos_tweets), len(neg_tweets)]
# plot 
plt.pie(size,labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 70)
# equal aspect ratio
plt.axis('equal')
# display
plt.show()

# looking at raq texts
# print('\033[92m' +  pos_tweets[random.randint(0,5000)])
# print('\033[91m' +  neg_tweets[random.randint(0,5000)])

# preprocessing raw texts for sentiment analysis

# choose a sample pos tweet
tweet = pos_tweets[random.randint(0,5000)]
# remove hyperlinks
tweet2 = re.sub(r'https?://[^\s\n\r]+', '', tweet)
# remove hashtags
tweet2 = 

