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

def sort_keys_by_value(dictionary, reverse_keys=True):
    """Sort keys of a given dictionary by its values. By default, from the highest
    value to the lowest.
    """
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse_keys))
    return sorted_dict

def dict_keys_values_into_two_lists(dictionary):
    """On the base of a given dictionary, two list are created. First of the list contains
    keys, the second of the list contains values.
    EXAMPLE: dictionary = {'a': 1, 'b': 2, 'c': 3} -> ['a', 'b', 'c'] ; [1, 2, 3]
    """
    dict_keys = []
    dict_values = []
    for key in dictionary.keys():
        dict_keys.append(key)
        dict_values.append(dictionary[key])
    return dict_keys, dict_values

def create_list_matrix(base_list):
    """Create a list matrix of a base list. The highest position(s) of the base list
    is/are assigned '1', next highest is/are assigned '2' and so on.
    EXAMPLE: base_list = [7, 7, 5, 2, 2, 1] -> list_matrix = [1, 1, 2, 3, 3, 4]
    """
    list_matrix = [1]
    i = 1
    for position in range(0, len(base_list) - 1):
        if base_list[position] == base_list[position + 1]:
            list_matrix.append(i)
        else:
            i += 1
            list_matrix.append(i)
    return list_matrix