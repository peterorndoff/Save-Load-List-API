#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify
import json
import os

flask_application = Flask(__name__)

saved_list = None
dir_path = os.path.dirname(os.path.realpath(__file__))


@flask_application.route('/')

def page():
    return render_template('index.html')


@flask_application.route('/data')

def data():
    
    json_url = os.path.join('data.json')
    data_json = json.load(open(json_url))
    return render_template('index.html',html_page_text=data_json)

@flask_application.route('/data_get', methods=['GET'])

def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)


@flask_application.route('/data_save', methods=['POST'])

def save_data():
    
    data = request.get_json()
    with open('data.json', 'w') as file:
        json.dump(data, file)
    return "List Saved"


if __name__ == '__main__':
    app.run(debug=True)
