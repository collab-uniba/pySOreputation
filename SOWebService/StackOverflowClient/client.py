# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:06:39 2019

@author: Roberto Bellarosa

"""

import requests
import json
"""
curl \
  --header "Content-type: application/json" \
  --request POST \
  --data '{"user_id": "1315221", "date": "2019-08-31"}' \
  http://127.0.0.1:19000/estimate
"""
def send_request_post():
    url = "http://127.0.0.1:19000/estimate"
    data = my_json.give_json()
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type':'application/json'})
    return response

