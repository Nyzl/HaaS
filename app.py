# This is the Flask app

import os
import logging
import json
from retrying import retry
from flask import Flask, render_template, request
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
@app.route('/', methods=['GET'])
def home():
    return render_template(
        'index.html', title='Home')


@app.route('/api')
def api():
    hexs = generator.generate_hex(6)
    hex_json = json.dumps(hexs, ensure_ascii=False)
    return hex_json


@app.route('/analytics', methods=['GET', 'POST'])
def analytics_ua():
    type = request.args.get('type', default='ua')
    ga_version = {'ua': 'GTM-5S9XWS6', 'ga4': 'GTM-TTVXKG3'}
    container_id = ga_version[type]
    if request.method == "POST":
        input = request.form['hex_count'] or '6'
        num = int(input)
    else:
        num = 6
    hexs = generator.generate_hex(num)
    hexagrams = ''
    for h in hexs:
        hexagrams += h['hex']
    readings = hexs
    return render_template(
        'index-a.html', container_id=container_id, title='Hexagrams', hexagrams=hexagrams, readings=readings)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
