# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:29:06 2019

@author: Roberto Bellarosa
"""
from parallel.workers import worker
from parallel.procData import preprocessing
from parallel.procData import get_basic_from_file
import datetime

def main():
    print("\nWelcome to Stack Overflow reputation estimator!")
    print("\nLoading data...\nIt will takes about 15 minutes!")
    start = datetime.datetime.now()
    the_map = preprocessing()
    basics = get_basic_from_file()
    end = datetime.datetime.now()
    print("Time to load: " + str(end-start))
    while True:
        decision = input("To start computation press c, else q to exit: ")
        if(decision == 'c'):
            worker(the_map,basics)
        elif(decision == 'q'):
            break
main()
