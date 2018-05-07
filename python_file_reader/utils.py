# -*- coding: utf-8 -*-

"""This is the utility file with all utility functions"""
__author__ = "Suraj Shah"
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Suraj Shah"
__email__ = "ssshah22@asu.edu"
__status__ = "Production"

import re
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
    """
    Generate a random string of capital characters of size 'size' that will be used as
    placeholder for the actual string with quotation marks, so that the 3 strings can be
    easily split by space
    :param size: int size of string
    :return: random string of size 'size'
    """
    return ''.join(choice(ascii_uppercase) for _ in range(size))


def separate_strings(record):
    """
    Separate the possibly given 3 input strings
    :param record: the entire record with spaces inside a string preserved
    :return: flag indicating if the record is valid, and if it is valid,
            return the string2
    """
    # The control comes here only if id and datetime are valid, hence remove
    # them and focus on the string
    record = record.split(None, 2)[-1]
    strings = re.findall('((?<!\\\)“.*?(?<!\\\)”)', record)
    str_len = len(strings)

    if str_len is 0 or str_len > 3:
        return False, None

    # Replacing detected strings with placeholders for easy separation
    temporary_map = {}
    for i in range(str_len):
        rand_string = generate_random_string(STRING_SIZE)
        record = record.replace(strings[i], rand_string)
        temporary_map[rand_string] = strings[i]

    # Now find string1 if valid else return False
    record_string_list = record.split()
    string_order_map = {}
    if len(record_string_list) == 3:
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
    # clean the record
    record = record.strip()
    record_values_list = record.split()
    if len(record_values_list) < 5:
        return False, ()

    # Check if id is unsigned positive number (considering whole numbers so 0 is a valid ID)
    if not record_values_list[0].isdigit():
        return False, ()

    # Check if the datetime is valid and in format. If not, it will throw a value error
    # and return False
    try:
        date_ = datetime.strptime(record_values_list[1], DATE_TIME_FORMAT)
    except ValueError:
        return False, ()

    # If record does not contain any quotes, then it splitting it should result in a list
    # of size 5.
    contains_quotes = re.findall("["+QUOTES+"]", record)
    if len(record_values_list) == 5 and not contains_quotes:
        return True, (record_values_list[0], record_values_list[3])

    # Call to the function that works on separating strings, act based on validity flag
    validity_flag, string2 = separate_strings(record)
    if validity_flag:
        return validity_flag, (record_values_list[0], string2)
    return False, ()


def validate_input(func):
    """This decorator validates input and sends only valid input
       back along with the count of invalid inputs"""
    def wrapper(*args, **kwargs):
        invalid_records_count = 0
        input_records = func(*args, **kwargs)

        validated_input_records = []
        for each_record in input_records:
            flag, record = is_valid_record(each_record)
            if flag:
                validated_input_records.append(record)
            else:
                # print(each_record)
                invalid_records_count += 1

        print("Found {} invalid records out of a total of {} records..."
              .format(invalid_records_count, len(input_records)))
        return validated_input_records
    return wrapper
