#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely.
    Args:
        fct: The function to execute.
        args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        func_result = fct(*args)
        return (func_result)
    except (ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
