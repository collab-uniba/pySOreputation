# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:24:46 2019

@author: Roberto Bellarosa
"""

from parallel.SOuser import SOuser
from parallel.procData import setup_all
from parallel.reputation import reputation
import concurrent.futures
import json
import datetime

##############################################################################
                             # Worker #
##############################################################################

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


def worker(the_map,basics,sousers):
    
    report = open("report.txt", "w+")
    report.close()
    report = open("report.txt", "a+")
    report.write("User id, preprocessing information time" + "\n")

    data = {}
    data['user'] = []
    
    temp = []
    for idx in range(len(sousers)):
        temp.append(setup_all(basics,sousers[idx]))
    sousers = temp

    report.write("User id, DisplayName, Begin date, End date, Reputation, Estimated reputation" + "\n")
    
    NUM_WORKERS = len(sousers)
    ct = NUM_WORKERS - 1
    process_time_in = datetime.datetime.now()
    futures = []
    saves = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        for _ in range(NUM_WORKERS):
            res = executor.submit(saves.append(reputation(sousers[ct],the_map)))
            ct = ct - 1
            futures.append(res)
        concurrent.futures.wait(futures)
    for save in saves:
        report.write(sousers[ct].get_all() + ", " + str(save)  + "\n")
        data['user'].append({'user_id':sousers[ct].get_id(),'user_name':sousers[ct].get_user(),
            'beginDate':sousers[ct].get_begin(),'reputation':str(sousers[ct].get_reputation()),
            'estimate':str(save)})        
        ct = ct - 1
    process_time_out = datetime.datetime.now()
    process_time = process_time_out - process_time_in
    data['timexe'] =str(process_time)
    report.write("Total time for concurrent.futures execution: " + str(process_time) + "\n")
        
    return data
