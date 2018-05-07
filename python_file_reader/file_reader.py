# -*- coding: utf-8 -*-
"""Mention details about file here"""
__author__ = "Suraj Shah"
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Suraj Shah"
__email__ = "ssshah22@asu.edu"
__status__ = "Production"


import os
from python_file_reader.utils import validate_input
BASEDIR = "python_file_reader"
INPUT_LOGS_DIRECTORY = os.path.join(BASEDIR, "log_files")


@validate_input
def read_input_files(file_name):
    """
    This function reads the input file(s) and returns all input lines
    :param args: is a filename
    :return: all input lines
    """
    input_file_names = []
    for name in os.listdir(INPUT_LOGS_DIRECTORY):
        if not name.endswith(".py"):
            input_file_names.append(name)
    if file_name and file_name in input_file_names:
        input_file_names = [file_name]

    input_log_records = []
    for input_file in input_file_names:
        with open(os.path.join(INPUT_LOGS_DIRECTORY, input_file), "r") as file_reader:
            input_log_records.extend(list(file_reader.readlines()))
    return input_log_records
