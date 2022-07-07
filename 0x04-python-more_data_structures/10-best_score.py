#!/usr/bin/python3

def best_score(a_dictionary):
    """ returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    _key = list(sorted(a_dictionary.values()))
    return(list(a_dictionary.keys())[list(a_dictionary.values()).index(_key[-1])])
