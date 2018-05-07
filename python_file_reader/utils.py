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
import math, re
from functools import reduce
import traceback
from random import choice
from string import ascii_uppercase
from datetime import datetime
DATE_TIME_FORMAT = "%Y-%m-%d-%H:%M:%S"
DOUBLE_QUOTE = '"'
LEFT_DOUBLE_QUOTE = '“'
RIGHT_DOUBLE_QUOTE = '”'
QUOTES_LIST = [DOUBLE_QUOTE, LEFT_DOUBLE_QUOTE, RIGHT_DOUBLE_QUOTE]
QUOTES = "".join(QUOTES_LIST)
STRING_SIZE = 128

def generate_random_string(size):
    return  ''.join(choice(ascii_uppercase) for _ in range(size))

def separate_strings(record):
    """
    Separate the possibly given 3 input strings
    :param record: the entire record with spaces inside a string preserved
    :return: flag indicating if the record is valid, and if it is valid,
            return the string2
    """
    record = record.split(None, 2)[-1]
    strings = re.findall('(“.*?(?<!\\\)”)', record)
    str_len = len(strings)
    # if str_len is 3:
    #     return True, strings[1]

    if str_len is 0 or str_len > 3:
        return False, None

    temporary_map = {}
    for i in range(str_len):
        rand_string = generate_random_string(STRING_SIZE)
        record = record.replace(strings[i], rand_string)
        temporary_map[rand_string] = strings[i]

    record_string_list = record.split()
    string_order_map = {}
    if len(record_string_list) is 3:
        for n, each_string in enumerate(record_string_list):
            if each_string in temporary_map.keys():
                string_order_map[n] = temporary_map[each_string]
            else:
                string_order_map[n] = each_string
        return True, string_order_map[1]

    return False, None


def is_valid_record(record):
    """
    Perform checks to find if the given records is valid or not
    First validate the id, then validate the date and then validate the three strings
    using regex
    :param record: a single string line of input
    :return: return a validity_flag of record along with a tuple of it's ID and string2
    """
    record = record.strip()
    record_values_list = record.split()
    # print(record_values_list)
    if len(record_values_list) < 5:
        return False, ()

    #check if id is unsigned positive number (considering whole numbers so 0 is a valid ID)
    if not record_values_list[0].isdigit():
        return False, ()

    try:
        date = datetime.strptime(record_values_list[1], DATE_TIME_FORMAT)
    except ValueError:
        return False, ()

    contains_quotes = re.findall("["+QUOTES+"]", record)
    if len(record_values_list) is 5 and not contains_quotes:
        return True, (record_values_list[0], record_values_list[3])
    #use a regex function here
    validity_flag, string2 = separate_strings(record)
    if validity_flag:
        return validity_flag, (record_values_list[0], string2)
    return False, ()


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
                    print(each_record)
                    invalid_records_count += 1

            print("Found {} invalid records out of a total of {} records...".format(invalid_records_count,
                                                                                    len(input_records)))
            if verbose_flag:
                print("\nAll records cleaned...")
            return validated_input_records
        return wrapper
    return validate_input