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
            json.dump(self.my_obj,write_file)
        
    def update_json(self, user_id, date):
        self.my_obj['user_id'].append(user_id)
        self.my_obj['date'].append(date)
        with open(self.file, "w") as write_file:
            json.dump(self.my_obj,write_file)
            
    def reset(self):
        self.my_obj['user_id'] = []
        self.my_obj['date'] = []
        with open(self.file, "w") as write_file:
            json.dump(self.my_obj,write_file)
    
    def is_null(self):
        if(len(self.my_obj['user_id']) == 0) and (len(self.my_obj['date']) == 0):
            is_empty = True
        else:
            is_empty = False
        return is_empty
    
    def give_json(self):
        return self.my_obj
