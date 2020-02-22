# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:07:34 2019

@author: Roberto Bellarosa
"""

import datetime

from flask import Flask, request, jsonify
from flask import g

from parallel.procData import get_basic_from_file
from parallel.procData import preprocessing
from parallel.workers import worker

app = Flask(__name__)


@app.route('/estimate', methods=['POST'])
def serv_reputation():
    the_json = request.get_json(force=True)
    so_users = decode_users(the_json)
    data = worker(the_map, basics, so_users)
    return jsonify(data)


def decode_users(json_data):
    so_users = dict()
    so_users[json_data['user_id']] = json_data['date']
    return so_users


def get_basic():
    if 'basics' not in g:
        g.basics = get_basic_from_file()
    return g.basics


def get_map():
    if 'the_map' not in g:
        g.the_map = preprocessing()
    return g.the_map


with app.app_context():
    print("\nBooting Stack Overflow reputation estimator web service")
    print("Loading data... (it will take about 10 minutes)\n")
    start = datetime.datetime.now()
    the_map = get_map()
    basics = get_basic()
    end = datetime.datetime.now()
    print("Time to load: " + str(end - start))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
