# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 23:38:49 2019

@author: Roberto Bellarosa
"""

import json


class data_handler:
    file = "data_file.json"

    def __init__(self):
        return

    def to_json(self):
        self.my_obj = {}
        self.my_obj['user_id'] = []
        self.my_obj['date'] = []
        with open(self.file, "w") as write_file:
            json.dump(self.my_obj, write_file)

    def update_json(self, user_id, date):
        self.my_obj['user_id'].append(user_id)
        self.my_obj['date'].append(date)
        with open(self.file, "w") as write_file:
            json.dump(self.my_obj, write_file)

    def reset(self):
        self.my_obj['user_id'] = []
        self.my_obj['date'] = []
        with open(self.file, "w") as write_file:
            json.dump(self.my_obj, write_file)

    def is_null(self):
        if (len(self.my_obj['user_id']) == 0) and (len(self.my_obj['date']) == 0):
            is_empty = True
        else:
            is_empty = False
        return is_empty

    def give_json(self):
        return self.my_obj

    def get_users(self):
        return self.my_obj['user_id']

    def get_dates(self):
        return self.my_obj['dates']

    def print_val(self):
        print(str(self.my_obj['user_id']))

# =============================================================================
# result_json = data_handler()
# result_json.to_json()
# 
# result_json.update_json("1196","2019-08-01")
# result_json.update_json("113455","2019-08-11")
# result_json.update_json("123345","2018-08-24")
# result_json.update_json("976443","2019-08-01")
# result_json.update_json("45345435","2014-07-01")
# result_json.update_json("35435345","2013-11-01")
# 
# result_json.print_val()
# =============================================================================
