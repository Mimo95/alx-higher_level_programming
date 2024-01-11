#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for value_d in list(a_dictionary.keys()):
        if value == a_dictionary.get(value_d):
            del a_dictionary[value_d]
    return (a_dictionary)
