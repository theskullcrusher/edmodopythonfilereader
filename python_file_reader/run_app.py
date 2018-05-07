#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Mention details about file here"""
__author__ = "Suraj Shah"
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Suraj Shah"
__email__ = "ssshah22@asu.edu"
__status__ = "Production"

import os, sys
import argparse
import math
from functools import reduce
import traceback
from time import time
from python_file_reader import file_reader
from python_file_reader.search_logs import SearchLogs

def main(args):
    """
    This method is a runner for the application
    :param args: is a dict with input file and verbose options
    :return: does not return anything
    """
    if args['verbose'].lower() is "true":
        file_reader.VERBOSE_FLAG = True

    validated_input_log_records = file_reader.read_input_files(args['file'])
    search_object = SearchLogs()
    search_object.insert_multiple(validated_input_log_records)
    ids = input("Please enter a comma separated list of ids to search for...\n")
    ids_list = ids.split(',')
    ids_list = [x.strip() for x in ids_list]
    output_tuple_list = search_object.search(ids_list)
    for id, string2 in output_tuple_list:
        print(id, string2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default=None)
    parser.add_argument('-v', '--verbose', default='false')
    args = vars(parser.parse_args())
    main(args)
