# Tweet Analysis Project under Coursera NLP Course

# Tokenize 
<!-- To Instantiate tokenize Class : -->
```
tokenizer = TweetTokenizer(preserve_case = False, strip_handles = True, reduce_len = True)
```
<!-- and then tokinze using : output = tokenizer.tokenize(input) -->

# Remove Stop words and punctuations           
<!-- import english stop words list. -->

```
stopwords_english = stopwords.words('english')
```
<!-- To create a clean list : -->
```
for word in tweet_tokens:
    if (word not in stopwords_english and word not in string.punctuation):
        tweet_clean.append(word)
```

