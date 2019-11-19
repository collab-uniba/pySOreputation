# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:05:24 2019

@author: Roberto Bellarosa
"""
from parallel.SOuser import SOuser
from parallel.procData import setup_all
from parallel.reputation import reputation
import concurrent.futures
import datetime

##############################################################################
                             # Worker #
##############################################################################

def worker(the_map,basics):
    
    report = open("report.txt", "w+")
    report.close()
    report = open("report.txt", "a+")
    report.write("User id, preprocessing information time" + "\n")
    
    sousers = []
    temp = ""
    i = 0
    while temp != 'q':
        if i == 0:
            temp = raw_input("Press q to close the program or press Enter to provide information about the user:")
        else:
            temp = raw_input("Press q to exit and start processing information or press enter to give another user: ")
        if temp == 'q':
            break
        else:
            single = SOuser()
            single = setup_all(basics)
            sousers.append(single)
            i = i + 1

    report.write("User id, DisplayName, Begin date, End date, Reputation, Estimated reputation" + "\n")
    
    NUM_WORKERS = i
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
        ct = ct - 1
    process_time_out = datetime.datetime.now()
    process_time = process_time_out - process_time_in
    report.write("Total time for concurrent.futures execution: " + str(process_time) + "\n")
    print("Time for concurrent.futures: " + str(process_time))
  
