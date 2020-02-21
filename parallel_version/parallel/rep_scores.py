# -*- coding: utf-8 -*-
"""
Created on Wed Nov  27 10:16:59 2019

@author: Roberto Bellarosa
"""


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
