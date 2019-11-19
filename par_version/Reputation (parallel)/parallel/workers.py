# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:05:24 2019

@author: Roberto Bellarosa
"""

from parallel.SOuser import SOuser
from parallel.procData import preprocessing
from parallel.procData import setup_all
from parallel.reputation import reputation
import concurrent.futures
import datetime
import pandas as pd

##############################################################################
                             # Worker #
##############################################################################

def create_dict(mother_set):
    start = datetime.datetime.now()  
  
    aindex = mother_set[0]
    qindex = mother_set[1]
    creationDates = mother_set[2]
    idx1 = mother_set[3]    
    dates1 = mother_set[4]   
    idx2 = mother_set[5]
    dates2 = mother_set[6]
    idx3 = mother_set[7]
    dates3 = mother_set[8]
    idx4 = mother_set[9]
    dates4 = mother_set[10]
    
    question_id = {}
    answer_id = {}
    up_quest_id = {}
    down_quest_id = {}
    up_answ_id = {}
    down_answ_id = {}
    
    ### Create a map key=user_id values=dates for answer accepted
    idx_dates = 0
    temp = []
    for user in aindex:
        if user in answer_id:
            temp = answer_id.get(user)
            temp.append(creationDates[idx_dates])
            answer_id[user] = temp
        else:
            temp.append(creationDates[idx_dates])
            answer_id[user] = temp
        idx_dates = idx_dates + 1
        temp = []
    
    ### Create a map key=user_id values=dates for question accepted 
    idx_dates = 0
    temp = []
    for user in qindex:
        if user in question_id:
            temp = question_id.get(user)
            temp.append(creationDates[idx_dates])
            question_id[user] = temp
        else:
            temp.append(creationDates[idx_dates])
            question_id[user] = temp
        idx_dates = idx_dates + 1
        temp = []
        
    ### Create a map key=user_id values=dates for question up voted
    idx_dates = 0
    temp = []
    for user in idx1:
        if user in up_quest_id:
            temp = up_quest_id.get(user)
            temp.append(dates1[idx_dates])
            up_quest_id[user] = temp
        else:
            temp.append(dates1[idx_dates])
            up_quest_id[user] = temp
        idx_dates = idx_dates + 1
        temp = []

    ### Create a map key=user_id values=dates for question down voted       
    idx_dates = 0
    temp = []
    for user in idx2:
        if user in down_quest_id:
            temp = down_quest_id.get(user)
            temp.append(dates2[idx_dates])
            down_quest_id[user] = temp
        else:
            temp.append(dates2[idx_dates])
            down_quest_id[user] = temp
        idx_dates = idx_dates + 1
        temp = []  
        
    ### Create a map key=user_id values=dates for answer up voted
    idx_dates = 0
    temp = []
    for user in idx3:
        if user in up_answ_id:
            temp = up_answ_id.get(user)
            temp.append(dates3[idx_dates])
            up_answ_id[user] = temp
        else:
            temp.append(dates3[idx_dates])
            up_answ_id[user] = temp
        idx_dates = idx_dates + 1
        temp = [] 

    ### Create a map key=user_id values=dates for answer down voted
    idx_dates = 0
    temp = []
    for user in idx4:
        if user in down_answ_id:
            temp = down_answ_id.get(user)
            temp.append(dates4[idx_dates])
            down_answ_id[user] = temp
        else:
            temp.append(dates4[idx_dates])
            down_answ_id[user] = temp
        idx_dates = idx_dates + 1
        temp = [] 
        
    mother_set = []
    big_map = []
    big_map.append(answer_id)
    big_map.append(question_id)
    big_map.append(up_quest_id)
    big_map.append(down_quest_id)
    big_map.append(up_answ_id)
    big_map.append(down_answ_id)
   
    end = datetime.datetime.now()
    print("Time for mapping: " + str(end-start))
    
    return big_map

def worker():
    
    #Pandas code
    
    report = open("report.txt", "w+")
    report.close()
    report = open("report.txt", "a+")
    report.write("User id, preprocessing information time" + "\n")
    
    mother_set = []
    
    start = datetime.datetime.now()
    print("Loading data ...")
    print("It may take about ten minutes!")
    file = "/mnt/vdb/bellarosa_tesi/SO_reputation/scripts/parallel/Users.csv"
    users = pd.read_csv(file, usecols = [0,1,2,3,11], header = None, sep = ',', quotechar = '"', index_col = [0], engine = 'c')
    users_index = users.index.values.tolist()
    names = users[3].tolist()
    dates = users[2].tolist()
    reputations = users[1].tolist()
    downvotes_list = users[11].tolist()
    
    file = "/mnt/vdb/bellarosa_tesi/SO_reputation/scripts/parallel/Question_Answer.csv"
    qa = pd.read_csv(file, usecols = [2,4,5], header = None, sep = ',', quotechar = '"', engine = 'c')
    aindex = qa[4].tolist()
    qindex = qa[2].tolist()
    creationDates = qa[5].tolist()
    
    file = "/mnt/vdb/bellarosa_tesi/SO_reputation/scripts/parallel/Posts_Votes1.csv"
    pv1 = pd.read_csv(file, usecols = [0,1], header = None, sep = ',', quotechar = '"', index_col = [0], engine = 'c')    
    idx1 = pv1.index.values.tolist()
    dates1 = pv1[1].tolist()
    
    file = "/mnt/vdb/bellarosa_tesi/SO_reputation/scripts/parallel/Posts_Votes2.csv"
    pv2 = pd.read_csv(file, usecols = [0,1], header = None, sep = ',', quotechar = '"', index_col = [0], engine = 'c')
    idx2 = pv2.index.values.tolist()
    dates2 = pv2[1].tolist()

    file = "/mnt/vdb/bellarosa_tesi/SO_reputation/scripts/parallel/Posts_Votes3.csv"
    pv3 = pd.read_csv(file, usecols = [0,1], header = None, sep = ',', quotechar = '"', index_col = [0], engine = 'c')
    idx3 = pv3.index.values.tolist()
    dates3 = pv3[1].tolist()
    
    file = "/mnt/vdb/bellarosa_tesi/SO_reputation/scripts/parallel/Posts_Votes4.csv"
    pv4 = pd.read_csv(file, usecols = [0,1], header = None, sep = ',', quotechar = '"', index_col = [0], engine = 'c')
    idx4 = pv4.index.values.tolist()
    dates4 = pv4[1].tolist()

    end = datetime.datetime.now()
    print("Time to preprocessing the data: " + str(end -start))

    mother_set.append(aindex)   
    mother_set.append(qindex)    
    mother_set.append(creationDates)
    mother_set.append(idx1)    
    mother_set.append(dates1)    
    mother_set.append(idx2)    
    mother_set.append(dates2)
    mother_set.append(idx3)
    mother_set.append(dates3)
    mother_set.append(idx4)
    mother_set.append(dates4)    
    
    data = []
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
            single = setup_all(users_index,names,dates,reputations,downvotes_list)
            sousers.append(single)
            i = i + 1

    report.write("User id, DisplayName, Begin date, End date, Reputation, Estimated reputation" + "\n")
    
    the_map = create_dict(mother_set)   

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
