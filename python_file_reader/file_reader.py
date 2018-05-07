#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Mention details about file here"""
__author__ = "Suraj Shah"
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Suraj Shah"
__email__ = "ssshah22@asu.edu"
__status__ = "Production"

"""Things to remember:
1. they will try to break it
2. Test input file for incoding type - binary or not?
3. Use consist tabs or 4 spaces
4. write cleandata validate data and elapsedtime decorators
5. Make code readable, check pylint score, 80char perline
6. For between classes use 2 newlines and between functions use one
7. Write unittests
8. Write comments"""

import os, sys
import argparse
import math
from functools import reduce
import traceback
from time import time
from python_file_reader.utils import validate_input_cover
BASEDIR = "python_file_reader"
INPUT_LOGS_DIRECTORY = os.path.join(BASEDIR,"log_files")
VERBOSE_FLAG = False


@validate_input_cover(VERBOSE_FLAG)
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
        with open(os.path.join(INPUT_LOGS_DIRECTORY, input_file), "r") as f:
            input_log_records.extend(list(f.readlines()))
    return input_log_records