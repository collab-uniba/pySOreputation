# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:07:34 2019

@author: Roberto Bellarosa
"""

import datetime

from flask import Flask, request
from flask import g

from parallel.SOuser import SOuser
from parallel.procData import get_basic_from_file
from parallel.procData import preprocessing
from parallel.workers import worker

app = Flask(__name__)


@app.route('/estimate', methods=['POST'])
def serv_reputation():
    the_json = request.get_json(force=True)
    sousers = decode_users(the_json)
    data = worker(the_map, basics, sousers)
    return data


def decode_users(json_data):
    sousers = []
    data = json_data
    users = data['user_id']
    dates = data['date']
    i = 0
    for item in users:
        single = SOuser()
        single.set_id(item)
        single.set_end(dates[i])
        sousers.append(single)
        i = i + 1
    return sousers


def get_basic():
    if 'basics' not in g:
        g.basics = get_basic_from_file()
    return g.basics


def get_map():
    if 'the_map' not in g:
        g.the_map = preprocessing()
    return g.the_map


with app.app_context():
    print("\nBooting Stack Overflow reputation estimator web service\n")
    print("Loading data... (it will take about 10 minutes)\n")
    start = datetime.datetime.now()
    the_map = get_map()
    basics = get_basic()
    end = datetime.datetime.now()
    print("Time to load: " + str(end - start))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
