# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:10:07 2019
Last modified on Feb 20, 2020

@author: Roberto Bellarosa, Fabio Calefato
"""
import argparse
import datetime  # library to manage date
import os
from typing import Optional, Any

import pymysql  # library to access MySQL


class Souser:
    def __init__(self):
        self.user_name = ""
        self.endDate = ""
        self.user_id = ""
        self.beginDate = ""
        self.reputation = 0
        self.estimated_reputation = 0
        return

    def set_user(self, user_name):
        self.user_name = user_name

    def set_end(self, d):
        self.endDate = d

    def set_id(self, user_id):
        self.user_id = user_id

    def set_begin(self, d):
        self.beginDate = d

    def get_user(self):
        return self.user_name

    def get_id(self):
        return self.user_id

    def get_begin(self):
        return self.beginDate

    def get_end(self):
        return self.endDate

    def get_reputation(self):
        return self.reputation

    def set_reputation(self, r):
        self.reputation = r

    def set_estimate_reputation(self, er):
        self.estimated_reputation = er

    def get_estimate_reputation(self):
        return self.estimated_reputation

    def get_all(self):
        user = str(self.get_id()) + "," + str(self.get_user()) + "," + str(self.get_begin()) + "," + str(self.get_end())
        user = user + "," + str(self.get_reputation()) + "," + str(self.get_estimate_reputation())
        return user

    def print(self):
        print(self.user_name)
        print(self.user_id)
        print(self.beginDate)
        print(self.endDate)


# This class provide the reputation scores values

class Score:

    def __init__(self):
        return

    quest_up = 10  # question is voted up: +10
    ans_up = 10  # answer is voted up: +10
    ans_accepted = 15  # answer is marked "accepted": +15
    acceptor = 2  # acceptor of the answer: +2
    quest_down = -2  # question is voted down: −2
    ans_down = -2  # your answer is voted down: −2


def setup_all(user_id, end_date):
    print(user_id, end_date)
    main_cursor.execute("select DisplayName from " + users_table + "  where Id = '" + user_id + "'")
    user_name = main_cursor.fetchone()[0]
    main_cursor.execute("select CreationDate from " + users_table + " where id = " + str(user_id))
    begin_date = main_cursor.fetchone()
    begin_date = begin_date[0].date()

    try:
        year, month, day = map(int, end_date.split('-'))
        end_date = datetime.date(year, month, day)
        if end_date >= begin_date:
            pass
        else:
            print("Warning: user {0} was not registered on {1} yet".format(str(user_id), str(end_date)))
    except ValueError as e:
        print(e)

    s = Souser()
    s.set_user(user_name)
    s.set_id(user_id)
    s.set_end(end_date)
    s.set_begin(begin_date)

    return s


def reputation(souser):
    main_cursor = conn.cursor()  # create a cursor to execute query
    main_cursor.execute("use " + database_name)  # access to database

    begin_date = souser.get_begin()
    end_date = souser.get_end()
    user_id = souser.get_id()

    print("##########################################################################################")
    print("Working for this user parameters: ")
    souser.print()

    start = datetime.datetime.now()

    print("Considering days from " + str(begin_date) + " to " + str(end_date))

    estimated_reputation = 1  # starting reputation (can't be below 1)
    bonus_flag = True

    main_cursor.execute("select reputation from " + users_table + " where Id = " + str(user_id))
    real_reputation = main_cursor.fetchone()
    real_reputation = real_reputation[0]
    souser.set_reputation(real_reputation)

    while begin_date <= end_date:

        search_day1 = begin_date.strftime('%Y-%m-%d') + " 00:00:00"
        search_day2 = begin_date.strftime('%Y-%m-%d') + " 23:59:59"
        daily_points = 0  # (You can earn a maximum of 200 reputation per day)
        bounty_awards = 0
        accepted_answers = 0
        main_cursor.execute(
            "select count(*) from question_answer where ACreationDate between '" + search_day1 + "' and '" + search_day2 + "' and AOwnerUserId = " + str(
                user_id) + " and QOwnerUserId <> " + str(user_id))
        result = main_cursor.fetchone()
        result = result[0]
        accepted_answers = accepted_answers + result * score.ans_accepted  # answer is marked “accepted”

        main_cursor.execute(
            "select count(*) from question_answer where ACreationDate between '" + search_day1 + "' and '" + search_day2 + "' and QOwnerUserId = " + str(
                user_id) + " and AOwnerUserId <> " + str(user_id))
        result = main_cursor.fetchone()
        result = result[0]
        accepted_answers = accepted_answers + result * score.acceptor  # to acceptor

        main_cursor.execute(
            "select count(*) from posts_votes1 where CreationDate = '" + str(begin_date) + "' and OwnerUserId = " + str(
                user_id))
        upvotes = main_cursor.fetchone()
        upvotes = upvotes[0]
        daily_points = daily_points + upvotes * score.quest_up  # question is voted up

        main_cursor.execute(
            "select count(*) from posts_votes2 where CreationDate = '" + str(begin_date) + "' and OwnerUserId = " + str(
                user_id))
        downvotes: Optional[Any] = main_cursor.fetchone()
        downvotes = downvotes[0]
        daily_points = daily_points + downvotes * score.quest_down  # your question is voted down

        main_cursor.execute(
            "select count(*) from posts_votes3 where CreationDate = '" + str(begin_date) + "' and OwnerUserId = " + str(
                user_id))
        upvotes = main_cursor.fetchone()
        upvotes = upvotes[0]
        daily_points = daily_points + upvotes * score.ans_up  # answer is voted up

        main_cursor.execute(
            "select count(*) from posts_votes4 where CreationDate = '" + str(begin_date) + "' and OwnerUserId = " + str(
                user_id))
        downvotes = main_cursor.fetchone()
        downvotes = downvotes[0]
        daily_points = daily_points + downvotes * score.ans_down  # your answer is voted down

        daily_points = daily_points + accepted_answers  # accepted answers are not subject to the daily reputation limit

        daily_points = daily_points + bounty_awards  # bounty awards are not subject to the daily reputation limit

        estimated_reputation = estimated_reputation + daily_points

        if estimated_reputation >= 200 and bonus_flag:
            estimated_reputation = estimated_reputation + 100
            bonus_flag = False

        if estimated_reputation < 1:  # reputation can never drop below 1
            estimated_reputation = 1

        begin_date = begin_date + datetime.timedelta(days=1)  # vado al giorno successivo

    main_cursor.execute("select DownVotes from " + users_table + " where Id = " + str(user_id))
    downvotes = main_cursor.fetchone()
    downvotes = downvotes[0]
    estimated_reputation = estimated_reputation + downvotes * -1  # you vote down an answer: −1

    if estimated_reputation < 1:
        estimated_reputation = 1
    end = datetime.datetime.now()
    souser.set_estimate_reputation(estimated_reputation)
    print("The estimated reputation at " + str(end_date) + " is: " + str(estimated_reputation) +
          " (registered reputation " + str(real_reputation) + ")")
    print("Time to estimate reputation for user " + str(user_id) + ": " + str(end - start))


def create_argparser():
    my_parser = argparse.ArgumentParser(description='Set id and date to estimate SO user reputation')
    my_parser.add_argument('-u', '--uid',
                           action='store',
                           type=str,
                           help='The id of the SO user')
    my_parser.add_argument('-f', '--file',
                           action='store',
                           type=str,
                           help='A text file containing a list of SO user ids, one per line)'
                           )
    my_parser.add_argument('-d', '--date',
                           action='store',
                           type=str,
                           required=True,
                           help='The date at which estimate the reputation (YYYY-MM-DD format, on or after 2012-04-05)')
    return my_parser


database_name = "stackoverflow"

badges_table = "badges"
comments_table = "comments"
post_history_table = "post_history"
post_links_table = "post_links"
posts_table = "posts"
tags_table = "tags"
users_table = "users"
votes_table = "votes"

# create a connection to MySQL with arguments: host, username and password
conn = pymysql.connect(host='localhost', user='user', password='password')
main_cursor = conn.cursor()
main_cursor.execute("use " + database_name)  # access to database

score = Score()


def main():
    parser = create_argparser()
    args = parser.parse_args()
    uid = args.uid
    date = args.date
    uid_file = args.file

    if uid is None and uid_file is None:
        raise Exception('Invalid parameters: either a single SO user id or a file with multiple ids must be provided')

    so_users = []
    i = 0
    if uid is not None:
        single_user = setup_all(uid, date)
        so_users.append(single_user)
        i = i + 1
    elif uid_file is not None:
        if not os.path.isfile(uid_file):
            raise ('The file specified does not exist')
        with open(uid_file, mode='r') as f:
            lines = f.readlines()
            for line in lines:
                u = line.strip().replace('"', '')
                if u.isdigit():
                    single_user = setup_all(u, date)
                    so_users.append(single_user)
                    i = i + 1

    num_workers = i

    report = open("seq_report.txt", "w+")
    report.close()
    report = open("seq_report.txt", "a+")
    report.write("User id, creation time, real reputation, estimated reputation, pre-processing information time\n")

    # Run tasks sequentially
    start_time = datetime.datetime.now()
    ct = len(so_users) - 1
    for _ in range(num_workers):
        of = so_users[ct]
        reputation(of)
        report.write(so_users[ct].get_all() + "\n")
        ct = ct - 1
    end_time = datetime.datetime.now()
    print("Total time: " + str(end_time - start_time))
    conn.close()


if __name__ == '__main__':
    main()
