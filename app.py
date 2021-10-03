from flask import Flask, render_template, request, jsonify, url_for
import requests
import os
import uuid
import json
from dotenv import load_dotenv
load_dotenv()
# url_for('static', filename='script.js')

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def dict_page():
    return render_template('dict.html')

@app.route('/translate', methods=['POST'])
def index_post():

    original_text = request.form['word']
    from_language = request.form['from']
    to_language = request.form['to']

    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']

    path = '/translate?api-version=3.0&'

    target_language_parameter = 'from=' + from_language + '&to=' + to_language

    constructed_url = endpoint + path + target_language_parameter

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{'text': original_text}]

    translator_request = requests.post(
        constructed_url, headers=headers, json=body)

    translator_response = translator_request.json()
    translated_text = translator_response[0]['translations'][0]['text']

    return jsonify(translated_text)

if __name__ == '__main__':
    app.run()
