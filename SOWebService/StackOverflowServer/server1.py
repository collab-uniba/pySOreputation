# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:07:34 2019

@author: Roberto Bellarosa
"""

from parallel.procData import preprocessing
from parallel.workers import worker
from parallel.procData import get_basic_from_file
from parallel.workers import decode_users
import datetime
from flask import Flask, request
from flask_restful import Resource, Api
from flask import g

app = Flask(__name__)

@app.route('/estimate', methods=['POST'])
def serv_reputation():
    the_json = request.get_json(force=True)
    sousers = decode_users(the_json)
    data = worker(the_map,basics,sousers)
    return data

def get_basic():
    if 'basics' not in g:
        g.basics = get_basic_from_file()
    return g.basics

def get_map():
    if 'the_map' not in g:
        g.the_map = preprocessing()
    return g.the_map

with app.app_context():
    print("\nWelcome to Stack Overflow reputation estimator!")
    print("\nLoading data...\nIt will takes about 15 minutes!")
    start = datetime.datetime.now()
    the_map = get_map()
    basics = get_basic()
    end = datetime.datetime.now()
    print("Time to load: " + str(end-start))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

