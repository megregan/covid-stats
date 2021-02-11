import logging
from flask import Flask
from flask_cors import CORS, cross_origin
import json
from flask import jsonify
import requests
import tweepy as tw
import nltk
#from nltk.stem import WordNetLemmatizer 
#from nltk.tokenize import TweetTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import regex as re
import traceback
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

root = os.path.dirname(os.path.abspath(__file__))
download_dir = os.path.join(root, 'nltk_data')
os.chdir(download_dir)
nltk.data.path.append(download_dir)


def get_tweets(key_word):
    # api key
    api_key = "zdsNjBDVPKStSJ5atDYXoYxx3"
    # api secret key
    api_secret_key = "TQ5JCoecU9mUcNeHL8Avuell9TMl1eKcX3ep91ycsWiMIe0ZqV"
    # access token
    access_token = "1086363611491115008-Do9ksI2Tk2cafLwVSsJ2EzgsOVItC3"
    # access token secret
    access_token_secret = "zADpXMs6q2dJlkFyLrVk3rr6K7phuJuiZfBjuO1QhQYHt"

    # authorize the API Key
    authentication = tw.OAuthHandler(api_key, api_secret_key)

    # authorization to user's access token and access token secret
    authentication.set_access_token(access_token, access_token_secret)

    # call the api
    api = tw.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    tweets = []
    #key_word +=  " -filter:retweets"
    c = 30
    tweet_raw = api.search(q=key_word, count=c)
    for tweet in tweet_raw:
            tweets.append(tweet.text)
    return(tweets)





def preprocess(tweet):
    #patterns to be removed [usernames,urls,punucuation/special chars, digits]
    patterns = [r"@[\w]*", r"http\S+", r'[\d]']
    for pattern in patterns:
        tweet = re.sub(pattern, '', tweet)
    #removing the # from the start of hashtags
    hashtags = re.finditer(r"#(\w+)",tweet)
    for tag in hashtags:
        tweet = re.sub(tag.group(0),tag.group(1),tweet)
    #initilising lemmatizer and tokenizer objects
    #lemmatizer = WordNetLemmatizer() 
    #preprocessed_tweet = [lemmatizer.lemmatize(word).lower() for word in tweet.split(' ')]
    preprocessed_tweet = [(word).lower() for word in tweet.split(' ')]
    return((' ').join(preprocessed_tweet))

def get_sentiment(tweets):
    vader = SentimentIntensityAnalyzer()
    scores = [vader.polarity_scores(tweet) for tweet in tweets] 
    pos = sum([1 for value in scores if value['compound'] >= 0])/len(tweets)
    neg = sum([1 for value in scores if value['compound'] < 0])/len(tweets)
    return pos,neg



@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/country/<country_code>')
@cross_origin()
def country_stats(country_code):
    url = "https://corona.lmao.ninja/v2/countries/" + country_code
    response = requests.get(url)
    return jsonify(response.json())
 
@app.route('/sentiment/<topic>')
@cross_origin()
def get_sentiment_api(topic):
    pos = 0
    try:
       print("get_sentiment_api start")
       topic = str(topic)
       raw_tweets = get_tweets(topic)
       tweets =[preprocess(tweet) for tweet in raw_tweets]
       pos, neg = get_sentiment(tweets)
       print("get_sentiment_api end")
       pos = str(pos)
       print("get_sentiment_api pos=" + pos)
    except Exception as e:
       print("get_sentiment_api error")
       tb = traceback.format_exc()
       print("get_sentiment_api tb=" + tb)
       return tb
    return pos

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
