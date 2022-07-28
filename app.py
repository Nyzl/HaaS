# This is the Flask app

import os
import logging
import json
from retrying import retry
from flask import Flask, render_template
from src import generator


app = Flask(__name__)
port = os.environ.get('PORT')


#  retry wrapper for functions
@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=10)
def retry_wrap(fn):
    try:
        fn
    except Exception as err:
        logging.error(err)
        raise err


#  define endpoints
@app.route('/')
def home():
    hexs = generator.generate_hex(6)
    hexagrams = ''
    for h in hexs:
        hexagrams += h['hex']
    readings = hexs
    return render_template('index.html', title='Home', hexagrams=hexagrams, readings=readings)


@app.route('/ascii_api')
def ascii_api():
    hexs = generator.generate_hex(6)
    hex_json = json.dumps(hexs)
    return hex_json


@app.route('/api')
def api():
    hexs = generator.generate_hex(6)
    hex_json = json.dumps(hexs, ensure_ascii=False)
    return hex_json


@app.route('/analytics_ua')
def analytics_ua():
    container_id = 'GTM-5S9XWS6'
    hexs = generator.generate_hex(6)
    hexagrams = ''
    for h in hexs:
        hexagrams += h['hex']
    readings = hexs
    return render_template('index-a.html', container_id=container_id, title='Home', hexagrams=hexagrams, readings=readings)


@app.route('/analytics_ga4')
def analytics_ga4():
    container_id = 'GTM-TTVXKG3'
    hexs = generator.generate_hex(6)
    hexagrams = ''
    for h in hexs:
        hexagrams += h['hex']
    readings = hexs
    return render_template('index-a.html', container_id=container_id, title='Home', hexagrams=hexagrams, readings=readings)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
