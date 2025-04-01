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

# labels
labels = np.append(np.ones((len(all_pos))), np.zeros((len(all_neg))))

# dictionaries
def build_freqs(tweets, ys):
    yslist =   np.squeeze(ys).tolist()

    freqs = {}
    for y, tweet in zip(yslist, tweets):
        for word in process_tweet(tweet):
            pair = (word, y)
            if pair in freqs:
                freqs[pair] += 1
            else:
                freqs[pair] = 1
    return freqs

freqs = build_freqs(tweets, labels)
print(f"Type : {type(freqs)}")
print(f"Len : {len(freqs)}")
# print(freqs)


# table of word counts
keys = ['happi', 'merri', 'nice', 'good', 'bad', 'sad', 'mad', 'best', 'pretti',
        '❤', ':)', ':(', '😒', '😬', '😄', '😍', '♛',
        'song', 'idea', 'power', 'play', 'magnific']

data = []
for word in keys:
    pos = 0
    neg = 0
    if (word,1) in freqs:
        pos = freqs[(word,1)]

    if (word,0) in freqs:
        neg = freqs[(word,0)]

    data.append([word,neg,pos])

print(data)

# Plots

fig, ax = plt.subplots(figsize = (8,8))

x = np.log([x[1] + 1 for x in data])
y = np.log([x[2] + 1 for x in data])

ax.scatter(x,y)

plt.xlabel("Log Positive")
plt.ylabel("Log Negative")

for i in range(0, len(data)):
    ax.annotate(data[i][0], (x[i], y[i]), fontsize = 12)

ax.plot([0,9], [0,9], color = 'red')
plt.show() 