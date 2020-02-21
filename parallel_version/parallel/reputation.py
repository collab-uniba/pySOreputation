# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:16:20 2019
Last modified on Feb 21, 2020 by Fabio Calefato

@author: Roberto Bellarosa
"""

import datetime  # library to manage date

from parallel.rep_scores import Score

score = Score()


def reputation(souser, big_map):
    start = datetime.datetime.now()
    answer_id = big_map[0]
    question_id = big_map[1]
    up_quest_id = big_map[2]
    down_quest_id = big_map[3]
    up_answ_id = big_map[4]
    down_answ_id = big_map[5]

    begin_date = souser.get_begin()
    end_date = souser.get_end()

    print("##########################################################################################")

    print("Considering days from " + str(begin_date) + " to " + str(end_date))
    estimated_reputation = 1  # starting reputation (can't be below 1)
    # edit_limit = 0
    bonus_flag = True

    real_reputation = souser.get_reputation()
    print("The real reputation is: ")
    print(str(real_reputation))

    result = 0

    while begin_date <= end_date:

        # print(str(begin_date) + " - " + str(end_date) + " - " + str(estimated_reputation) + " - " + str(real_reputation))
        search_day1 = begin_date.strftime('%Y-%m-%d') + " 00:00:00"
        search_day2 = begin_date.strftime('%Y-%m-%d') + " 23:59:59"
        daily_points = 0  # (You can earn a maximum of 200 reputation per day)
        bounty_awards = 0
        accepted_answers = 0

        qa1 = answer_id.get(souser.get_id())
        result = 0
        if qa1 is not None:
            for i in qa1:
                if i >= search_day1:
                    if i <= search_day2:
                        result = result + 1

        accepted_answers = accepted_answers + result * score.ans_accepted  # answer is marked “accepted”: +15

        qa2 = question_id.get(souser.get_id())
        result = 0
        if qa2 is not None:
            for j in qa2:
                if j >= search_day1:
                    if j <= search_day2:
                        result = result + 1

        accepted_answers = accepted_answers + result * score.acceptor  # (+2 to acceptor)

        temp = begin_date
        begin_date = str(begin_date) + " 00:00:00"

        upvotes_count = 0
        pv1 = up_quest_id.get(souser.get_id())
        if pv1 != None:
            for k in pv1:
                if k == begin_date:
                    upvotes_count = upvotes_count + 1

        daily_points = daily_points + upvotes_count * score.quest_up  # question is voted up: +5

        downvotes = 0
        pv2 = down_quest_id.get(souser.get_id())
        if pv2 is not None:
            for l in pv2:
                if l == begin_date:
                    downvotes = downvotes + 1

        daily_points = daily_points + downvotes * score.quest_down  # your question is voted down: -2

        upvotes_count = 0
        pv3 = up_answ_id.get(souser.get_id())
        if pv3 is not None:
            for m in pv3:
                if m == begin_date:
                    upvotes_count = upvotes_count + 1

        daily_points = daily_points + upvotes_count * score.ans_up  # answer is voted up: +10

        downvotes = 0
        pv4 = down_answ_id.get(souser.get_id())
        if pv4 is not None:
            for n in pv4:
                if n == begin_date:
                    downvotes = downvotes + 1

        daily_points = daily_points + downvotes * score.ans_down  # your answer is voted down: -2

        daily_points = daily_points + accepted_answers  # accepted answers are not subject to the daily reputation limit

        daily_points = daily_points + bounty_awards  # bounty awards are not subject to the daily reputation limit

        estimated_reputation = estimated_reputation + daily_points

        if estimated_reputation >= 200 and bonus_flag:
            estimated_reputation = estimated_reputation + 100
            bonus_flag = False

        if estimated_reputation < 1:  # reputation can never drop below 1
            estimated_reputation = 1

        begin_date = temp
        begin_date = begin_date + datetime.timedelta(days=1)  # going to next day

    downvotes = souser.get_downVotes()

    # cast to integer downvotes if use pandas
    estimated_reputation = estimated_reputation + int(downvotes) * -1  # you vote down an answer: −1

    if estimated_reputation < 1:
        estimated_reputation = 1

    print("The estimated reputation on " + str(end_date) + " is: " + str(
        estimated_reputation) + " while the real reputation is : " + str(real_reputation))
    end = datetime.datetime.now()
    print("Time for estimate reputation for this user " + str(souser.get_id()) + " :")
    print(end - start)
    return estimated_reputation
