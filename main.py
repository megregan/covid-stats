import logging
from flask import Flask
from flask_cors import CORS, cross_origin
import json
from flask import jsonify
import requests

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/global')
@cross_origin()
def global_stats():
    url = "https://thevirustracker.com/free-api?global=stats"
    response = requests.get(url)
    return jsonify(response.json())

@app.route('/country/<country_code>')
@cross_origin()
def country_stats(country_code):
    url = "https://corona.lmao.ninja/v2/countries/" + country_code
    response = requests.get(url)
    return jsonify(response.json())

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500



