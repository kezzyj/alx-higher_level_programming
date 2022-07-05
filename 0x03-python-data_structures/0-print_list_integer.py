#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Write a function that prints all integers of a list."""
    count = len(my_list) - 1
    for index in range(count):
        print("{:d}".format(my_list[index])
