#!/usr/bin/python

def pow(a, b):
    """computes a to the power of b and return the value."""
    pow = 0
    for index in range(1,b):
        pow += a * a
    return pow

