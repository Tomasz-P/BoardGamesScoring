"""Functions that enable operations on a dictionary data structure."""


# FUNCTIONS

def inner_to_outer_dict(dictionary):
    """Convert an outer dictionary with outer keys and ddictionaries (with inner keys and inner
    values) as outer values into a new dictionary. New dictionary has inner keys as new keys and
    dictionaries (with outer keys and inner values) as new values.
    EXAMPLE: outer_dict = {'A':{'a':1,'b':2}, 'B':{'a':2, 'c':5}}
    new_outer_dict = {'a':{'A':1,'B':2}, 'b':{'A':2, 'B':0}, 'c':{'A':0, 'B':5}}
    """
    outer_keys = []
    inner_keys = []
    for outer_key in dictionary.keys():
        outer_keys.append(outer_key)
        for inner_key in dictionary[outer_key].keys():
            if inner_key not in inner_keys:
                inner_keys.append(inner_key)
    new_outer_dict = {}
    for inner_key in inner_keys:
        new_inner_dict = {}
        for outer_key in outer_keys:
            if inner_key in dictionary[outer_key]:
                new_inner_dict[outer_key] = dictionary[outer_key][inner_key]
            else:
                new_inner_dict[outer_key] = 0
        new_outer_dict[inner_key] = new_inner_dict
    return new_outer_dict