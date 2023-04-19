#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new = {}
        tmp = {}
        for key, value in a_dictionary.items():
            new_val = value * 2
            tmp = {key: new_val}
            new.update(tmp)
        return (new)
    return None

