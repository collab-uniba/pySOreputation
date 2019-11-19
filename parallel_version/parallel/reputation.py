# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:16:20 2019

@author: Roberto Bellarosa
"""

import datetime # library to manage date
from parallel.procData import preprocessing
  
def reputation(SOuser,big_map):
    
    start = datetime.datetime.now()
    answer_id = big_map[0] 
    question_id = big_map[1] 
    up_quest_id = big_map[2]
    down_quest_id = big_map[3]
    up_answ_id = big_map[4]
    down_answ_id = big_map[5]

        
    beginDate = SOuser.get_begin()
    endDate = SOuser.get_end()
        
    print("##########################################################################################")

    print("There will be considered days from " + str(beginDate) + " to " + str(endDate))
    estimated_reputation = 1 # starting reputation (can't be below 1)
    #edit_limit = 0
    bonus_flag = True

    real_reputation = SOuser.get_reputation()
    print("The real reputation is: ")
    print(str(real_reputation))

    result = 0
                
    while beginDate <= endDate:

        #print(str(beginDate) + " - " + str(endDate) + " - " + str(estimated_reputation) + " - " + str(real_reputation))
        searchDay1 = beginDate.strftime('%Y-%m-%d') + " 00:00:00"
        searchDay2 = beginDate.strftime('%Y-%m-%d') + " 23:59:59"
        daily_points = 0 # (You can earn a maximum of 200 reputation per day)
        bounty_awards = 0
        acceptedAnswers = 0

        qa1 = answer_id.get(SOuser.get_id())
        result = 0
        if(qa1 != None):
            for i in qa1:
                if(i >= searchDay1):
                    if(i <= searchDay2):
                        result = result + 1

        acceptedAnswers = acceptedAnswers + result * 15 #answer is marked “accepted”: +15
        
        qa2 = question_id.get(SOuser.get_id())
        result = 0
        if(qa2 != None):
            for j in qa2:
                if(j >= searchDay1):
                    if(j <= searchDay2):
                        result = result + 1
        
        acceptedAnswers = acceptedAnswers + result * 2 #(+2 to acceptor)
        
        temp = beginDate
        beginDate = str(beginDate) + " 00:00:00"
        
        upVotes = 0
        pv1 = up_quest_id.get(SOuser.get_id())
        if(pv1 != None):
            for k in pv1:
                if(k == beginDate):
                    upVotes = upVotes + 1

        daily_points = daily_points + upVotes * 5 #question is voted up: +5

        downVotes = 0
        pv2 = down_quest_id.get(SOuser.get_id())
        if(pv2 != None): 
            for l in pv2:
                if(l == beginDate):
                    downVotes = downVotes + 1               
                
        daily_points = daily_points + downVotes * -2 #your question is voted down: -2

        upVotes = 0
        pv3 = up_answ_id.get(SOuser.get_id())
        if(pv3 != None):
            for m in pv3:
                if(m == beginDate):
                    upVotes = upVotes + 1
        
        daily_points = daily_points + upVotes * 10 #answer is voted up: +10

        downVotes = 0
        pv4 = down_answ_id.get(SOuser.get_id())
        if(pv4 != None):
            for n in pv4:
                if(n == beginDate):
                    downVotes = downVotes + 1
        
        daily_points = daily_points + downVotes * -2 #your answer is voted down: -2
        

        daily_points = daily_points + acceptedAnswers #accepted answers are not subject to the daily reputation limit

        daily_points = daily_points + bounty_awards #bounty awards are not subject to the daily reputation limit

        estimated_reputation = estimated_reputation + daily_points

        if estimated_reputation >= 200 and bonus_flag:
            estimated_reputation = estimated_reputation + 100
            bonus_flag = False

        if estimated_reputation < 1: #reputation can never drop below 1
            estimated_reputation = 1
 
        beginDate = temp        
        beginDate = beginDate + datetime.timedelta(days = 1) #going to next day

    downVotes = SOuser.get_downVotes()
    
    #cast to integer downVotes if use pandas
    estimated_reputation = estimated_reputation + int(downVotes) * -1 #you vote down an answer: −1

    if estimated_reputation < 1:
        estimated_reputation = 1
            
    print("The estimated reputation on " + str(endDate) + " is: " + str(estimated_reputation) + " while the real reputation is : " + str(real_reputation))
    end = datetime.datetime.now()
    print("Time for estimate reputation for this user " + str(SOuser.get_id()) + " :")
    print(end - start)
    return estimated_reputation
