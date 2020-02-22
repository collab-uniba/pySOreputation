# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:16:56 2019

@author: Roberto Bellarosa
"""

class SOuser:
    def __init__(self):
        return
    
    def set_id(self, user_id):
        self.user_id = user_id

    def set_user(self,user_name):
        self.user_name = user_name
        
    def set_reputation(self, reputation):
        self.reputation = reputation

    def set_begin(self, d):
        self.beginDate = d

    def set_end(self, d):
        self.endDate = d
        
    def get_id(self):
        return self.user_id

    def get_user(self):
        return self.user_name
    
    def get_reputation(self):
        return self.reputation

    def get_begin(self):
        return self.beginDate

    def get_end(self):
        return self.endDate
    
    def set_downvotes(self, dv):
        self.downVotes = dv
    
    def get_downvotes(self):
        return self.downVotes
                   
    def get_all(self):
        user = str(self.get_id()) + "," + str(self.get_user()) + "," + str(self.get_begin()) + "," + str(self.get_end())
        user = user + "," + str(self.get_reputation())
        return user
    
    def print(self):
        print("DisplayName: " + self.user_name)
        print("Id: " + self.user_id)
        print("CreationDate: " + self.beginDate)
        print(self.endDate)
        print("Reputation: " + self.reputation)
