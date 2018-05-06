#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Mention details about file here"""
__author__ = "Suraj Shah"
__copyright__ = ""
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Suraj Shah"
__email__ = "ssshah22@asu.edu"
__status__ = "Production"

import os, sys
import argparse
import math, re
from functools import reduce
import traceback
from datetime import datetime
DATE_TIME_FORMAT = "%Y-%m-%d-%H:%M:%S"
DOUBLE_QUOTE = '"'
LEFT_DOUBLE_QUOTE = '“'
RIGHT_DOUBLE_QUOTE = '”'
QUOTES_LIST = [DOUBLE_QUOTE, LEFT_DOUBLE_QUOTE, RIGHT_DOUBLE_QUOTE]
QUOTES = "".join(QUOTES_LIST)

def is_valid_record(record):
    """
    Perform checks to find if the given records is valid or not
    :param record: a single string line of input
    :return: return a validity_flag of record along with a tuple of it's ID and string2
    """
    record_values_list = record.strip().split()
    # print(record_values_list)
    if len(record_values_list) < 5:
        return False, ()

    #check if id is unsigned positive number (considering whole numbers so 0 is a valid ID)
    if not record_values_list[0].isdigit():
        return False, ()

    try:
        date_ = datetime.strptime(record_values_list[1], DATE_TIME_FORMAT)
    except ValueError:
        return False, ()

    contains_quotes = re.match("["+QUOTES+"]", record)
    if len(record_values_list) is 5 and not contains_quotes:
        return True, (record_values_list[0], record_values_list[3])

    #use a regex function here



def validate_input_cover(verbose_flag):
    """Outer function on decorator just to pass it verbose flag"""
    def validate_input(func):
        """This decorator validates input and sends only valid input back along with the count of invalid inputs"""
        def wrapper(*args, **kwargs):
            invalid_records_count = 0
            input_records = func(*args, **kwargs)
            if verbose_flag:
                print("Cleaning input for valid records...")

            validated_input_records = []
            for each_record in input_records:
                flag, record = is_valid_record(each_record)
                if flag:
                    validated_input_records.append(record)
                else:
                    invalid_records_count += 1

            print("Found {} invalid records out of a total of {} records...".format(invalid_records_count,
                                                                                    len(input_records)))
            if verbose_flag:
                print("\nAll records cleaned...")
            return validated_input_records
        return wrapper
    return validate_input