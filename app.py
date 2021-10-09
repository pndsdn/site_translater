from flask import Flask, render_template, request, jsonify
import requests
import os
import uuid
import json
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def dict_page():
    return render_template('dict.html')


@app.route('/translate', methods=['POST'])
def index_post():
    original_text = request.json['translate'].lower()  # получаем значение из запроса по ключу 'translate'
    print(original_text)
    from_language = request.json['from']  # получаем значение из запроса по ключу 'from'
    print(from_language)
    to_language = request.json['to']  # получаем значение из запроса по ключу 'to'
    print(to_language)

    # здесь создаётся ссылка для запроса
    key = os.environ['KEY']                # значения key,
    endpoint = os.environ['ENDPOINT']      # endpoint,
    location = os.environ['LOCATION']      # location берутся из файла .env
    path = '/translate?api-version=3.0&'
    target_language_parameter = 'from=' + from_language + '&to=' + to_language  # часть ссылки, которая отвечает за параметры перевода
    constructed_url = endpoint + path + target_language_parameter  # готовая ссылка

    # заголовки обязательно передаются в запросе
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{'text': original_text}]  # тело запроса
    translator_response = requests.post(constructed_url, headers=headers, json=body)  # запрос
    return translator_response.json()  # возвращаем в виде JSON


if __name__ == '__main__':
    app.run()
