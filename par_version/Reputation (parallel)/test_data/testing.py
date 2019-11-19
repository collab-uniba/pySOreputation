# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:56:52 2019

@author: Roberto Bellarosa
"""

import csv
from parallel.SOuser import SOuser
import datetime
from parallel.reputation import reputation
import concurrent.futures

#date of download of dump
endDate = "2019-08-01"
year, month, day = map(int, endDate.split('-'))
endDate = datetime.date(year, month, day)

hdd_path1 = "C:\\Users\\Roberto Bellarosa\\Desktop\\new_users25.csv"
hdd_path2 = "C:\\Users\\Roberto Bellarosa\\Desktop\\low_users25.csv"
hdd_path3 = "C:\\Users\\Roberto Bellarosa\\Desktop\\established_users25.csv"
hdd_path4 = "C:\\Users\\Roberto Bellarosa\\Desktop\\trusted_users25.csv"

ssd_path1 = "F:\\new_users25.csv"
ssd_path2 = "F:\\low_users25.csv"
ssd_path3 = "F:\\established_users25.csv"
ssd_path4 = "F:\\trusted_users25.csv"

def preprocessing(user_id, param): #preprocessing all info about the user   
    infos = []
    if(param == 1): #preprocessing Question_Answer.csv
        with open("F:\\Question_Answer.csv", encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            for row in csv_reader:
                if(row[4] == user_id):
                    infos.append(row[5])
    elif(param == 2): #preprocessing Question_Answer.csv
        with open("F:\\Question_Answer.csv", encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            for row in csv_reader:
                if(row[2] == user_id):
                    infos.append(row[5])
    elif(param == 3): #preprocessing Posts_Votes1.csv
        with open("F:\\Posts_Votes1.csv", encoding="utf8") as csv_file3:
            csv_reader = csv.reader(csv_file3, delimiter = ',')
            for row in csv_reader:
                if(row[0] == user_id):
                    infos.append(row[1])
    elif(param == 4): #preprocessing Posts_Votes2.csv
        with open("F:\\Posts_Votes2.csv", encoding="utf8") as csv_file4:
            csv_reader = csv.reader(csv_file4, delimiter = ',')
            for row in csv_reader:
                if(row[0] == user_id):
                    infos.append(row[1])
    elif(param == 5): #preprocessing Posts_Votes3.csv
        with open("F:\\Posts_Votes3.csv", encoding="utf8") as csv_file5:
            csv_reader = csv.reader(csv_file5, delimiter = ',')
            for row in csv_reader:
                if(row[0] == user_id):
                    infos.append(row[1])
    elif(param == 6): #preprocessing Posts_Votes4.csv
        with open("F:\\Posts_Votes4.csv", encoding="utf8") as csv_file6:
            csv_reader = csv.reader(csv_file6, delimiter = ',')
            for row in csv_reader:
                if(row[0] == user_id):
                    infos.append(row[1])
    return infos

new_users = []
with open(ssd_path1, encoding = "utf-8") as file1:
    csv_reader = csv.reader(file1, delimiter = ',')
    for row in csv_reader:
        single = SOuser()
        single.set_id(row[0])
        single.set_user(row[1])
        single.set_reputation(row[2])
        begin_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
        begin_date = begin_date.date()
        single.set_begin(begin_date)
        single.set_downVotes(row[4])
        single.set_end(endDate)
        new_users.append(single)

low_users = []
with open(ssd_path2, encoding = "utf-8") as file1:
    csv_reader = csv.reader(file1, delimiter = ',')
    for row in csv_reader:
        single = SOuser()
        single.set_id(row[0])
        single.set_user(row[1])
        single.set_reputation(row[2])
        begin_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
        begin_date = begin_date.date()
        single.set_begin(begin_date)
        single.set_downVotes(row[4])
        single.set_end(endDate)
        low_users.append(single)

established_users = []       
with open(ssd_path3, encoding = "utf-8") as file1:
    csv_reader = csv.reader(file1, delimiter = ',')
    for row in csv_reader:
        single = SOuser()
        single.set_id(row[0])
        single.set_user(row[1])
        single.set_reputation(row[2])
        begin_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
        begin_date = begin_date.date()
        single.set_begin(begin_date)
        single.set_downVotes(row[4])
        single.set_end(endDate)
        established_users.append(single)

trusted_users = []
with open(ssd_path4, encoding = "utf-8") as file1:
    csv_reader = csv.reader(file1, delimiter = ',')
    for row in csv_reader:
        single = SOuser()
        single.set_id(row[0])
        single.set_user(row[1])
        single.set_reputation(row[2])
        begin_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
        begin_date = begin_date.date()
        single.set_begin(begin_date)
        single.set_downVotes(row[4])
        single.set_end(endDate)
        trusted_users.append(single)    
    
#Sequential preprocessing because machine bottleneck on I/O (hard disk)
data = []
micro_files = []
i = 0

for item in trusted_users:
    process_time_in = datetime.datetime.now()
    micro_files.append(preprocessing(item.take_id(),1))
    micro_files.append(preprocessing(item.take_id(),2))
    micro_files.append(preprocessing(item.take_id(),3))
    micro_files.append(preprocessing(item.take_id(),4))
    micro_files.append(preprocessing(item.take_id(),5))
    micro_files.append(preprocessing(item.take_id(),6))
    data.append(micro_files)
    micro_files = []
    process_time_out = datetime.datetime.now()
    process_time = process_time_out - process_time_in
    #report.write(item.take_all() + "," + str(process_time) + "\n")
    print("Time for preprocessing information: " + str(process_time) + " Id user " + str(item.take_id()))
    i = i + 1

#concurrent.futures for threading
NUM_WORKERS = i
ct = NUM_WORKERS - 1
process_time_in = datetime.datetime.now()
futures = []
with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
    for _ in range(NUM_WORKERS):
        res = executor.submit(reputation(trusted_users[ct],data[ct]))
        ct = ct - 1
        futures.append(res)
    concurrent.futures.wait(futures)
process_time_out = datetime.datetime.now()
process_time = process_time_out - process_time_in
print("Time for concurrent.futures: " + str(process_time))
