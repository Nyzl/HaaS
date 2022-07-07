# This is the Flask app

import os, logging
from retrying import retry
from flask import Flask, request, render_template, Response, stream_with_context
from src import generator

app = Flask(__name__)
port = os.environ.get('PORT') 



#  retry wrapper for functions
@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000,stop_max_attempt_number=10)
def retry_wrap(fn):
    try:
        fn
    except Exception as err:
        logging.error(err)
        #print(str(err))
        raise err


#  define endpoints
@app.route('/')
def home():
    #logo = generator.generate_hex(0)
    hexs = generator.generate_hex(6)
    hexagrams = ''.join(hexs[0])
    readings = hexs[1]
    return render_template('index.html', title='Home', hexagrams=hexagrams, readings=readings)

@app.route('/somewhereelse')
def somewhereelse():
    print("hello")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))