#!/usr/bin/python3

def best_score(a_dictionary):
     """ returns a key with the biggest integer value."""
     if not isinstance(a_dictionary, dict) and len(a_dictionary.keys()) == 0:
         return None
     _key = list(sorted(a_dictionary.values()))
     return(ret[-1])
