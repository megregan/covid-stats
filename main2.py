import logging
from flask import Flask
from flask_cors import CORS, cross_origin
import json
from flask import jsonify
import requests
import tweepy as tw

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
    api = tw.API(authentication, wait_on_rate_limit=True)
    key_word +=  " -filter:retweets"
    count = 30
    tweets = [tweet.text for tweet in api.search(q=key_word, count=count) if tweet.lang == "en"]
    return(tweets)


@app.route('/sentiment/<word>')
@cross_origin()
def sentiment(word):
    tweets = get_tweets(word)
    return  tweets

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500



