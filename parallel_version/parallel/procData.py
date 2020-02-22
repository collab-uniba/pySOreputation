# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:55:01 2019

@author: Roberto Bellarosa
"""

import datetime

import pandas as pd

from parallel.SOuser import SOuser


def is_int(s):
    return s.isdigit()


def get_username_by_id(uid, ids, names):
    name = None
    j = 0
    for i in ids:
        if i == int(uid):
            name = names[j]
            break
        j += 1

    if name is None:
        print("Warning, could not find a display bame for user {0}".format(uid))
        name = "Not-found"
    return name


def get_registration_date(user_id, ids, dates):
    temp = ""
    j = 0
    for i in ids:
        if i == int(user_id):
            temp = dates[j]
            break
        j += 1

    if temp == "":
        print("Warning, could not find registration date for user {0}".format(user_id) +
              "\nAssuming 2002-08-01 00:00:00")
        temp = "2002-08-01 00:00:00"
    temp = datetime.datetime.strptime(temp, '%Y-%m-%d %H:%M:%S')
    temp = temp.date()
    return temp


def get_reputation(user_id, ids, reputations):
    temp = ""
    j = 0
    for i in ids:
        if i == user_id:
            temp = reputations[j]
            break
        j += 1

    return temp


def get_downvotes(user_id, ids, downvotes_list):
    downvotes = 0
    j = 0
    for i in ids:
        if i == user_id:
            downvotes = downvotes_list[j]
            if type(downvotes) == str:
                downvotes = 0
                break
            break
        j = j + 1
    return downvotes


def setup_all(basics, user_id, end_date):
    uids = basics[0]
    names = basics[1]
    dates = basics[2]
    reputations = basics[3]
    upvotes_list = basics[4]
    downvotes_list = basics[5]

    user_name = get_username_by_id(user_id, uids, names)
    begin_date = get_registration_date(user_id, uids, dates)

    s = SOuser()
    s.set_user(str(user_name))
    s.set_id(str(user_id))
    s.set_end(end_date)
    s.set_begin(begin_date)
    s.set_reputation(get_reputation(user_id, uids, reputations))
    s.set_downVotes(get_downvotes(user_id, uids, downvotes_list))
    return s


def create_dict(mother_set):
    a_index = mother_set[0]
    q_index = mother_set[1]
    creation_dates = mother_set[2]
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

    # Create a map key=user_id values=dates for answer accepted
    idx_dates = 0
    temp = []
    for user in a_index:
        if user in answer_id:
            temp = answer_id.get(user)
            temp.append(creation_dates[idx_dates])
            answer_id[user] = temp
        else:
            temp.append(creation_dates[idx_dates])
            answer_id[user] = temp
        idx_dates = idx_dates + 1
        temp = []

    # Create a map key=user_id values=dates for question accepted
    idx_dates = 0
    temp = []
    for user in q_index:
        if user in question_id:
            temp = question_id.get(user)
            temp.append(creation_dates[idx_dates])
            question_id[user] = temp
        else:
            temp.append(creation_dates[idx_dates])
            question_id[user] = temp
        idx_dates = idx_dates + 1
        temp = []

    # Create a map key=user_id values=dates for question up voted
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

    # Create a map key=user_id values=dates for question down voted
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

        # Create a map key=user_id values=dates for answer up voted
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

        # Create a map key=user_id values=dates for answer down voted
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

    big_map = list()
    big_map.append(answer_id)
    big_map.append(question_id)
    big_map.append(up_quest_id)
    big_map.append(down_quest_id)
    big_map.append(up_answ_id)
    big_map.append(down_answ_id)

    return big_map


def get_basic_from_file():
    file = "./Users.csv"
    users = pd.read_csv(file, #usecols=[0, 1, 2, 3, 11],
                        header=None, error_bad_lines=False, sep=',', quotechar='"',
                        index_col=[0], engine='c')
    users_index = users.index.values.tolist()
    names = users[3].tolist()
    dates = users[2].tolist()
    reputations = users[1].tolist()
    upvotes_list = users[4].tolist
    downvotes_list = users[5].tolist()
    basics = list()
    basics.append(users_index)
    basics.append(names)
    basics.append(dates)
    basics.append(reputations)
    basics.append(upvotes_list)
    basics.append(downvotes_list)
    return basics


def preprocessing():  # preprocessing all info about the user  with pandas
    file0 = "./Question_Answer.csv"
    file1 = "./Posts_Votes1.csv"
    file2 = "./Posts_Votes2.csv"
    file3 = "./Posts_Votes3.csv"
    file4 = "./Posts_Votes4.csv"

    # Pandas code
    mother_set = list()

    qa = pd.read_csv(file0, usecols=[2, 4, 5], header=None, sep=',', quotechar='"', engine='c')
    a_index = qa[4].tolist()
    q_index = qa[2].tolist()
    creation_dates = qa[5].tolist()

    pv1 = pd.read_csv(file1, usecols=[0, 1], header=None, sep=',', quotechar='"', index_col=[0], engine='c')
    idx1 = pv1.index.values.tolist()
    dates1 = pv1[1].tolist()

    pv2 = pd.read_csv(file2, usecols=[0, 1], header=None, sep=',', quotechar='"', index_col=[0], engine='c')
    idx2 = pv2.index.values.tolist()
    dates2 = pv2[1].tolist()

    pv3 = pd.read_csv(file3, usecols=[0, 1], header=None, sep=',', quotechar='"', index_col=[0], engine='c')
    idx3 = pv3.index.values.tolist()
    dates3 = pv3[1].tolist()

    pv4 = pd.read_csv(file4, usecols=[0, 1], header=None, sep=',', quotechar='"', index_col=[0], engine='c')
    idx4 = pv4.index.values.tolist()
    dates4 = pv4[1].tolist()

    mother_set.append(a_index)
    mother_set.append(q_index)
    mother_set.append(creation_dates)
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
