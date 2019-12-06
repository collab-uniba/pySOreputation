# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:10:07 2019

@author: Roberto Bellarosa
"""

import os
import time
import datetime # library to manage date
import pymysql # library to access MySQL

class Souser:
    def __init__(self):
        return
   
    def set_user(self,user_name):
        self.user_name = user_name
   
    def set_end(self, endDate):
        self.endDate = endDate
    
    def set_id(self, user_id):
        self.user_id = user_id
        
    def set_begin(self, beginDate):
        self.beginDate = beginDate
        
    def get_user(self):
        return self.user_name
     
    def get_id(self):
        return self.user_id

    def get_end(self):
        return self.end_date
    
    def get_begin(self):
        return self.beginDate
     
    def get_end(self):
        return self.endDate
    
    def get_reputation(self):
        return self.reputation

    def set_reputation(self, reputation):
        self.reputation = reputation

    def set_estimate_reputation(self, estimated_reputation):
        self.estimated_reputation = estimated_reputation
        
    def get_estimate_reputation(self):
        return self.estimated_reputation

    def get_all(self):
        user = str(self.get_id()) + "," + str(self.get_user()) + "," + str(self.get_begin()) + "," + str(self.get_end())
        user = user + "," + str(self.get_reputation()) + "," + str(self.get_estimate_reputation())
        return user

    def printus(self):
	print(self.user_name)
	print(self.user_id)
	print(self.beginDate)
	print(self.endDate)    
        
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


database_name = "stackoverflow"

badges_table = "badges"
comments_table = "comments"
post_history_table = "post_history"
post_links_table = "post_links"
posts_table = "posts"
tags_table = "tags"
users_table = "users"
votes_table = "votes"

conn = pymysql.connect(host='localhost', user='insert_user', password='insert_password') # create a connection to MySQL with arguments: host, username and password
main_cursor = conn.cursor()
cursor = conn.cursor()
main_cursor.execute("use " + database_name) # access to database 

def setup_all():
    s = Souser()
    ris = []

    while True:
        user_name = input("Enter user name: ")
        main_cursor.execute("select Id from " + users_table + "  where DisplayName = '" + user_name + "'")
        x = main_cursor.fetchone()
        while x != None:
            x = int(x[0])
            ris.append(x)
            x = main_cursor.fetchone()

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
            user_id = input("Select the user's id: ")
            if RepresentsInt(user_id) == True:
                user_id = int(user_id)
                if user_id >= 0 and user_id <= len(ris):
                    break

        user_id = ris[user_id]

    else:
        user_id = ris[0]
        
    main_cursor.execute("select CreationDate from " + users_table + " where id = " + str(user_id))
    beginDate = main_cursor.fetchone()
    beginDate = beginDate[0].date()
    while True:
        try:
            endDate = input("Enter a date >= " + str(beginDate) + " in YYYY-MM-DD format: ")
            year, month, day = map(int, endDate.split('-'))
            endDate = datetime.date(year, month, day)
            if endDate >= beginDate:
                break
            else:
                print("Sorry, the user was not registered on " + str(endDate) + " yet!")
        except ValueError as e:
            print(e)
    
    s.set_user(user_name)
    s.set_id(user_id)
    s.set_end(endDate)
    s.set_begin(beginDate)
    
    return s
    
def reputation(Souser):

    main_cursor = conn.cursor() # create a cursor to execute query
    main_cursor.execute("use " + database_name) # access to database
    cursor = conn.cursor()
    
    beginDate = Souser.get_begin()
    endDate = Souser.get_end()
    user_id = Souser.get_id()
    
    print("##########################################################################################")
    print("Working for this user parameters: ")
    Souser.printus()

    start = datetime.datetime.now()

    print("There will be considered days from " + str(beginDate) + " to " + str(endDate))

    estimated_reputation = 1 # starting reputation (can't be below 1)
    edit_limit = 0
    bonus_flag = True

    main_cursor.execute("select reputation from " + users_table + " where Id = " + str(user_id))
    real_reputation = main_cursor.fetchone()
    real_reputation = real_reputation[0]
    Souser.set_reputation(real_reputation)

    while beginDate <= endDate:
        
        searchDay1 = beginDate.strftime('%Y-%m-%d') + " 00:00:00"
        searchDay2 = beginDate.strftime('%Y-%m-%d') + " 23:59:59"
        daily_points = 0 # (You can earn a maximum of 200 reputation per day)
        bounty_awards = 0
        acceptedAnswers = 0
        main_cursor.execute("select count(*) from question_answer where ACreationDate between '" + searchDay1 + "' and '" + searchDay2 + "' and AOwnerUserId = " + str(user_id) + " and QOwnerUserId <> " + str(user_id))
        result = main_cursor.fetchone()
        result = result[0]
        acceptedAnswers = acceptedAnswers + result * 15 #answer is marked “accepted”: +15

        main_cursor.execute("select count(*) from question_answer where ACreationDate between '" + searchDay1 + "' and '" + searchDay2 + "' and QOwnerUserId = " + str(user_id) + " and AOwnerUserId <> " + str(user_id))
        result = main_cursor.fetchone()
        result = result[0]
        acceptedAnswers = acceptedAnswers + result * 2 #(+2 to acceptor)

        main_cursor.execute("select count(*) from posts_votes1 where CreationDate = '" + str(beginDate) + "' and OwnerUserId = " + str(user_id))
        upVotes = main_cursor.fetchone()
        upVotes = upVotes[0]
        daily_points = daily_points + upVotes * 5 #question is voted up: +5

        main_cursor.execute("select count(*) from posts_votes2 where CreationDate = '" + str(beginDate) + "' and OwnerUserId = " + str(user_id))
        downVotes = main_cursor.fetchone()
        downVotes = downVotes[0]
        daily_points = daily_points + downVotes * -2 #your question is voted down: -2

        main_cursor.execute("select count(*) from posts_votes3 where CreationDate = '" + str(beginDate) + "' and OwnerUserId = " + str(user_id))
        upVotes = main_cursor.fetchone()
        upVotes = upVotes[0]
        daily_points = daily_points + upVotes * 10 #answer is voted up: +10

        main_cursor.execute("select count(*) from posts_votes4 where CreationDate = '" + str(beginDate) + "' and OwnerUserId = " + str(user_id))
        downVotes = main_cursor.fetchone()
        downVotes = downVotes[0]
        daily_points = daily_points + downVotes * -2 #your answer is voted down: -2

        daily_points = daily_points + acceptedAnswers #accepted answers are not subject to the daily reputation limit

        daily_points = daily_points + bounty_awards #bounty awards are not subject to the daily reputation limit

        estimated_reputation = estimated_reputation + daily_points

        if estimated_reputation >= 200 and bonus_flag:
            estimated_reputation = estimated_reputation + 100
            bonus_flag = False

        if estimated_reputation < 1: #reputation can never drop below 1
            estimated_reputation = 1

        beginDate = beginDate + datetime.timedelta(days = 1) #vado al giorno successivo

    main_cursor.execute("select DownVotes from " + users_table + " where Id = " + str(user_id))
    downVotes = main_cursor.fetchone()
    downVotes = downVotes[0]
    estimated_reputation = estimated_reputation + downVotes * -1 #you vote down an answer: −1
	
    if estimated_reputation < 1:
        estimated_reputation = 1
    end = datetime.datetime.now()
    Souser.set_estimate_reputation(estimated_reputation)
    print("The estimated reputation on " + str(endDate) + " is: " + str(estimated_reputation) + " while the real reputation is : " + str(real_reputation))
    print("Time to estimate reputation for user " + str(user_id) + ": " + str(end - start))

# The Main

sousers = []
temp = ""
i = 0
while temp != 'q':
    temp = input("Please press q to exit or press Enter to continue: ")
    if temp == 'q':
        break
    else:
        single = Souser()
        single = setup_all()
	sousers.append(single)
        i = i + 1

NUM_WORKERS = i

report = open("seq_report.txt", "w+")
report.close()
report = open("seq_report.txt", "a+")
report.write("User id, creation time, real reputation, estimated reputation, preprocessing information time" + "\n")

#Run tasks serially
start_time = datetime.datetime.now()
ct = len(sousers) - 1
for _ in range(NUM_WORKERS):
    of = sousers[ct]
    reputation(of)
    report.write(sousers[ct].get_all() + "\n")
    ct = ct - 1    
end_time = datetime.datetime.now()
print("Total time: " + str(end_time - start_time))
conn.close()
