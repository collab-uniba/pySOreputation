# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:55:01 2019

@author: Roberto Bellarosa
"""

import datetime
from parallel.SOuser import SOuser

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
    
    end = datetime.datetime.now()   
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
	    if(type(downVotes) == str):
                downVotes = 0
                break
            break
        j = j + 1
    return downVotes;

def setup_all(users_index,names,dates,reputations,downvotes_list):
    
    s = SOuser()
    ris = []
    while True:

        user_name = raw_input("Insert user name and press Enter: ")
        ris = getInfoUser(user_name, users_index,names)

        if len(ris) > 0:
            break
        else:
            print("Sorry, there's no user with that name!")

    if len(ris) > 1:
        while True:
            i = 0
            for item in ris:
                print(str(i) + " - " + str(item))
                i = i + 1
            user_id = raw_input("Select the user's id: ")
            if RepresentsInt(user_id) == True:
                user_id = int(user_id)
                if user_id >= 0 and user_id <= len(ris):
                    break

        user_id = ris[user_id]
        print("The user id is: " + str(user_id))

    else:
        user_id = ris[0]

    beginDate = getbeginDate(user_id, users_index, dates)

    while True:
        try:
            endDate = raw_input("Enter a date >= " + str(beginDate) + " in YYYY-MM-DD format: ")
            year, month, day = map(int, endDate.split('-'))
            endDate = datetime.date(year, month, day)
            if endDate >= beginDate:
                break
            else:
                print("Sorry, the user was not registered on " + str(endDate) + " yet!")
        except ValueError as e:
            print(e)
        
    s.set_user(str(user_name))
    s.set_id(str(user_id))
    s.set_end(endDate)
    s.set_begin(beginDate)
    s.set_reputation(getReputation(user_id, users_index,reputations))
    s.set_downVotes(getDownVotes(user_id, users_index,downvotes_list))
    return s

def preprocessing(user_id, param, mother_set): #preprocessing all info about the user  with pandas 
    infos = []
    if(param == 1): #preprocessing Question_Answer.csv
        aindex = mother_set[0]
        for item in aindex:
            if(item == user_id):
                infos.append(creationDates[i])
            i = i + 1
    elif(param == 2): #preprocessing Question_Answer.csv
        qindex = mother_set[1]
        creationDates = mother_set[2]
        i = 0
        for item in qindex:
            if(item == user_id):
                infos.append(creationDates[i])
            i = i + 1
    elif(param == 3): #preprocessing Posts_Votes1.csv
        idx1 = mother_set[3]
        dates1 = mother_set[4]
        i = 0
        for item in idx1:
            if(item == user_id):
                infos.append(dates1[i])
            i = i + 1
    elif(param == 4): #preprocessing Posts_Votes2.csv
        idx2 = mother_set[5]
        dates2 = mother_set[6]
        i = 0
        for item in idx2:
            if(item == user_id):
                infos.append(dates2[i])
            i = i + 1    
    elif(param == 5): #preprocessing Posts_Votes3.csv
        idx3 = mother_set[7]
        dates3 = mother_set[8]
        i = 0
        for item in idx3:
            if(item == user_id):
                infos.append(dates3[i])
            i = i + 1
    elif(param == 6): #preprocessing Posts_Votes4.csv
        idx4 = mother_set[9]
        dates4 = mother_set[10]
        i = 0
        for item in idx4:
            if(item == user_id):
                infos.append(dates4[i])
            i = i + 1
    return infos
