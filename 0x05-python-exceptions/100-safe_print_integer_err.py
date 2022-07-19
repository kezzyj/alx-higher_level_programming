#!/usr/bin/python3

import sys


def safe_print_integer_err(value):

    """function that prints an integer.
    Args:
        valu: integer to be printed

    Returns: true if value is integer and printed
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
