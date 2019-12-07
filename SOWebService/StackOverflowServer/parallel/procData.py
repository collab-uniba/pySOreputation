# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:24:26 2019

@author: Roberto Bellarosa
"""

import datetime
from parallel.SOuser import SOuser
import pandas as pd

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def getInfoUser(user_id,ids,names):
    ris = [] 
    j = 0
    for i in names:
        if (i == user_id):    
            ris.append(ids[j])
        j = j + 1
    return ris

def getbeginDate(user_id,ids,dates):
    temp = ""
    j = 0
    for i in ids:
        if (i == user_id):    
            temp = dates[j]
            break
        j = j + 1
    temp = datetime.datetime.strptime(temp, '%Y-%m-%d %H:%M:%S')
    temp = temp.date()
    return temp

def getReputation(user_id, ids, reputations):
    temp = ""   
    j = 0
    for i in ids:
        if (i == user_id):    
            temp = reputations[j]
            break
        j = j + 1    
    return temp

def getDownVotes(user_id, ids, downvotes_list):
    downVotes = 0
    j = 0
    for i in ids:
        if (i == user_id):    
            downVotes = downvotes_list[j]
            if (type(downVotes) == str):
                downVotes = 0
                break
            break
        j = j + 1
    return downVotes;

def setup_all(basics,s):

    users_index = basics[0]
    names = basics[1]
    dates = basics[2]
    reputations = basics[3]
    downvotes_list = basics[4]
    
    user_name = ""

    i = 0
    for user in users_index:
        if(user == s.get_id()):
            user_name = names[i]
            break
        i = i + 1
    
    beginDate = getbeginDate(s.get_id(), users_index, dates)
    endDate = s.get_end()
    year, month, day = map(int, endDate.split('-'))
    endDate = datetime.date(year, month, day)

    s.set_user(user_name)
    s.set_end(endDate)
    s.set_begin(beginDate)
    s.set_reputation(getReputation(s.get_id(), users_index,reputations))
    s.set_downVotes(getDownVotes(s.get_id(), users_index,downvotes_list))
    return s

def create_dict(mother_set):

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
    
    return big_map

def get_basic_from_file():
    file5 = "/Users.csv"
    users = pd.read_csv(file5, usecols = [0,1,2,3,11], error_bad_lines=False, header = None, sep = ',', quotechar = '"', index_col = [0], engine = 'c')
    users_index = users.index.values.tolist()
    names = users[3].tolist()
    dates = users[2].tolist()
    reputations = users[1].tolist()
    downvotes_list = users[11].tolist()
    basics = []
    basics.append(users_index)
    basics.append(names)
    basics.append(dates)
    basics.append(reputations)
    basics.append(downvotes_list)
    return basics
    

def preprocessing(): #preprocessing all info about the user  with pandas
    
    file0 = "/Question_Answer.csv"
    file1 = "/Posts_Votes1.csv"
    file2 = "/Posts_Votes2.csv"
    file3 = "/Posts_Votes3.csv"
    file4 = "/Posts_Votes4.csv"   
    
    #Pandas code    
    mother_set = []
         
    qa = pd.read_csv(file0, usecols = [2,4,5], header = None, sep = ',', quotechar = '"', engine = 'c')
    aindex = qa[4].tolist()
    qindex = qa[2].tolist()
    creationDates = qa[5].tolist()
    
    pv1 = pd.read_csv(file1, usecols = [0,1], header = None, sep = ',', quotechar = '"', index_col = [0], engine = 'c')    
    idx1 = pv1.index.values.tolist()
    dates1 = pv1[1].tolist()
    
    pv2 = pd.read_csv(file2, usecols = [0,1], header = None, sep = ',', quotechar = '"', index_col = [0], engine = 'c')
    idx2 = pv2.index.values.tolist()
    dates2 = pv2[1].tolist()

    pv3 = pd.read_csv(file3, usecols = [0,1], header = None, sep = ',', quotechar = '"', index_col = [0], engine = 'c')
    idx3 = pv3.index.values.tolist()
    dates3 = pv3[1].tolist()
    
    pv4 = pd.read_csv(file4, usecols = [0,1], header = None, sep = ',', quotechar = '"', index_col = [0], engine = 'c')
    idx4 = pv4.index.values.tolist()
    dates4 = pv4[1].tolist()

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
    
    the_map = create_dict(mother_set)
        
    return the_map 
