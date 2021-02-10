import logging
from flask import Flask
from flask_cors import CORS, cross_origin
import json
from flask import jsonify
import requests
#import tweepy as tw
#from nltk.corpus import stopwords
#from nltk.stem import WordNetLemmatizer 
#from nltk.tokenize import TweetTokenizer
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
#import regex as re

#tweepy
#nltk
#regex

app = Flask(__name__)

## api key
#api_key = "zdsNjBDVPKStSJ5atDYXoYxx3"
## api secret key
#api_secret_key = "TQ5JCoecU9mUcNeHL8Avuell9TMl1eKcX3ep91ycsWiMIe0ZqV"
## access token
#access_token = "1086363611491115008-Do9ksI2Tk2cafLwVSsJ2EzgsOVItC3"
## access token secret
#access_token_secret = "zADpXMs6q2dJlkFyLrVk3rr6K7phuJuiZfBjuO1QhQYHt"
#
## authorize the API Key
#authentication = tw.OAuthHandler(api_key, api_secret_key)
#
## authorization to user's access token and access token secret
#authentication.set_access_token(access_token, access_token_secret)
#
## call the api
#api = tw.API(authentication, wait_on_rate_limit=True)
#
#def get_tweets(key_word):
#    tweets = []
#    key_word +=  " -filter:retweets"
#    count = 30
#    for tweet in api.search(q=key_word, count=count):
#            tweets.append(tweet.text)
#    return(tweets)
#
#def preprocess(tweet):
#    #patterns to be removed [usernames,urls,punucuation/special chars, digits]
#    patterns = [r"@[\w]*", r"http\S+", r'[\d]']
#    for pattern in patterns:
#        tweet = re.sub(pattern, '', tweet)
#    #removing the # from the start of hashtags
#    hashtags = re.finditer(r"#(\w+)",tweet)
#    for tag in hashtags:
#        tweet = re.sub(tag.group(0),tag.group(1),tweet)
#    #initilising lemmatizer and tokenizer objects
#    lemmatizer = WordNetLemmatizer() 
#    stop_words = set(stopwords.words('english'))
#    preprocessed_tweet = [lemmatizer.lemmatize(word).lower() for word in tweet.split(' ') if word not in stop_words]
#    return((' ').join(preprocessed_tweet))
#
#def get_sentiment(tweets):
#    vader = SentimentIntensityAnalyzer()
#    scores = [vader.polarity_scores(tweet) for tweet in tweets] 
#    pos = sum([1 for value in scores if value >= 0])/len(tweets)
#    neg = sum([1 for value in scores if value < 0])/len(tweets)
#    return pos,neg

    
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/country/<country_code>')
@cross_origin()
def country_stats(country_code):
    url = "https://corona.lmao.ninja/v2/countries/" + country_code
    response = requests.get(url)
    return jsonify(response.json())

#@app.route('/sentiment/<topic>')
#@cross_origin()
#def country_stats(topic):
#    raw_tweets = get_tweets(topic)
#    tweets =[preprocess(tweet) for tweet in raw_tweets]
#    pos, neg = get_sentiment(tweets)
#    return pos

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500



