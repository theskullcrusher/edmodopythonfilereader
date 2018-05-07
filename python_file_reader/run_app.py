# -*- coding: utf-8 -*-
"""This file is the entry point of the application"""
__author__ = "Suraj Shah"
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Suraj Shah"
__email__ = "ssshah22@asu.edu"
__status__ = "Production"


import argparse
from python_file_reader import file_reader
from python_file_reader.search_logs import SearchLogs


def main(arguments):
    """
    This method is a runner for the application
    :param arguments: is a dict with input file and verbose options
    :return: does not return anything
    """
    validated_input_log_records = file_reader.read_input_files(arguments['file'])
    search_object = SearchLogs()
    search_object.insert_multiple(validated_input_log_records)
    ids = input("Please enter a comma separated list of ids to search for...\n")
    ids_list = ids.split(',')
    ids_list = [x.strip() for x in ids_list]
    output_tuple_list = search_object.search(ids_list)
    if output_tuple_list:
        print("\nQuery result:")
        for id_, string2 in output_tuple_list:
            print(id_, string2)
    else:
        print("\nNo results found!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default=None)
    args = vars(parser.parse_args())
    main(args)
