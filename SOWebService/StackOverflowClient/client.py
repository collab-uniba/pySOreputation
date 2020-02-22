# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:06:39 2019

@author: Roberto Bellarosa

"""
from data_handler import data_handler
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
    url = "http://127.0.0.1:8000/estimate"
    data = my_json.give_json()
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type':'application/json'})
    return response

def get_data(users, dates):
    while True:
        number = input("Insert user id: ")
        number = int(number)
	users.append(number)
        date = input("Insert a date in format YY-MM-DD:")
        dates.append(str(date))
        decision = input("To exit and start computation press q:")
        if(decision == 'q'):
	    break
        else:
            continue

my_json = data_handler()
my_json.to_json()

users = []
dates = []

get_data(users, dates)

i = 0
for item in users:
    my_json.update_json(item,dates[i])
    i = i + 1

resp = send_request_post()
data = resp.json()

my_json.reset()	

for i in data['user']:
    print("Result: ")
    print("User name: " + i['user_name'])
    print("User id: " + str(i['user_id']))
    print("Begin date: " + str(i['beginDate'])[:-12])
    print("Real reputation: " + str(i['reputation']))
    print("Estimate reputation: " + str(i['estimate']))
print("Total time for execution: " + data['timexe'])
