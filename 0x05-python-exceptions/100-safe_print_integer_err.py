#!/usr/bin/python3

def safe_print_integer_err(value):
    """function that prints an integer.
    Args:
        valu: integer to be printed

    Returns: true if value is integer and printed
    """
    import sys

    try:
        print("{:d}".format(value))
        return (true)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exec_info()[1]), file=sys.stderr)
        return (false)
