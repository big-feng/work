#!/usr/bin/python
#coding=utf8
"""
This is the "netster.py" module and it provides one function called print_lol()
 which prnts lists that may or may not include nested list."""

def print_lol(the_list):
    """This function tokes one positional argument called "the_list",which is any python
        list(of - possible - nested lists). Each data item in the provided list
        is (recursively) printed to the screen on it's own line."""

    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)