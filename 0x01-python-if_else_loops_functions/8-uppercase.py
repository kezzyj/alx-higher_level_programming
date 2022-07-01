#!/usr/bin/python3
# 8-uppercase.py
def uppercase(str):
     """Print a string in uppercase."""
     for index in str:
         if(ord(index) >= 97 and ord(index) <= 122):
             index = chr(ord(index) - 32)
         print("{}".format(index), end="")
     print(end = "")
