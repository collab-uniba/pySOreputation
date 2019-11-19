# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:29:06 2019

@author: Roberto Bellarosa
"""

import time
from parallel.workers import worker

def main():
    print("Welcome to Stack Overflow reputation estimator!")
    time.sleep(2)
    worker()
    
main()