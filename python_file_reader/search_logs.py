#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Mention details about file here"""
__author__ = "Suraj Shah"
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Suraj Shah"
__email__ = "ssshah22@asu.edu"
__status__ = "Production"


class SearchLogs:

    def __init__(self):
        self.memory_map = {}

    def insert_multiple(self, input_tuple_list):
        """
        Add a list of tuple entries to the in-memory map datastructure where tuple consists
        of (id, string2)
        :param input_tuple_list: list of tuples of the form (id, string2)
        :return: None
        """
        for id, string2 in input_tuple_list:
            if id in self.memory_map:
                self.memory_map[id].append(string2)
            else:
                self.memory_map[id] = [string2]

    def search(self, ids_list):
        """
        For a given list of ids, return all valid tuples of (id, string2)
        :param ids_list: list of positive integer ids as string values
        :return: list of tuples of the form (id, string2)
        """
        output_tuple_list = []
        for id in ids_list:
            if id in self.memory_map:
                for string2 in self.memory_map[id]:
                    output_tuple_list.append((id, string2))
        return output_tuple_list