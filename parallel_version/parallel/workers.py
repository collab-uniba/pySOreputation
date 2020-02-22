# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:05:24 2019
Last modified on Feb 21, 2020

@author: Roberto Bellarosa
"""
import concurrent.futures
import datetime

from parallel.procData import setup_all
from parallel.reputation import reputation


def worker(the_map, basics, so_users_dict):
    report = open("report.txt", "w+")
    report.close()
    report = open("report.txt", "a+")
    report.write("User id, DisplayName, Begin date, End date, Reputation, Estimated reputation\n")

    so_users = []
    i = 0
    for uid, date in so_users_dict.items():
        single_user = setup_all(basics, uid, date)
        so_users.append(single_user)
        i = i + 1

    num_workers = i
    ct = num_workers - 1
    process_time_in = datetime.datetime.now()
    futures = []
    saves = []
    data = dict()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        for _ in range(num_workers):
            res = executor.submit(saves.append(reputation(so_users[ct], the_map)))
            ct = ct - 1
            futures.append(res)
        concurrent.futures.wait(futures)
    for save in saves:
        report.write(so_users[ct].get_all() + ", " + str(save) + "\n")
        data[so_users[ct]] = str(save)
        ct = ct - 1
    process_time_out = datetime.datetime.now()
    process_time = process_time_out - process_time_in
    print("Time for concurrent.futures: " + str(process_time))
    return data
