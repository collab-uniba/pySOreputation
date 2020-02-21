# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:29:06 2019
Last modified on Feb 21, 2020 by Fabio Calefato

@author: Roberto Bellarosa
"""
import argparse
import datetime
import os

from parallel.procData import get_basic_from_file
from parallel.procData import preprocessing
from parallel.workers import worker

ids_input = []
single_input = []


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


def main():
    print("\nLoading data...\nIt will take about 15 minutes!")
    start = datetime.datetime.now()
    the_map = None
    basics = None
    the_map = preprocessing()
    basics = get_basic_from_file()
    end = datetime.datetime.now()
    print("Time to load: " + str(end - start))

    parser = create_argparser()
    args = parser.parse_args()
    uid = args.uid
    date = args.date
    file = args.file

    if uid is None and file is None:
        raise Exception('Invalid parameters: either a single SO user id or a file with multiple ids must be provided')

    so_users = dict()
    if uid is not None:
        so_users[uid] = date
    elif file is not None:
        if not os.path.isfile(file):
            raise ('The file specified does not exist')
        with open(file, mode='r') as f:
            lines = f.readlines()
            for line in lines:
                u = line.strip().replace('"', '')
                if u.isdigit():
                    so_users[u] = date
                    i = i + 1

    worker(the_map, basics, so_users)


if __name__ == '__main__':
    main()
