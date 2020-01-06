"""Functions that enable operations on a directory data structure."""


# FUNCTIONS

def inner_to_outer_dir(directory):
    """Convert an outer directory with outer keys and directories (with inner keys and inner
    values) as outer values into a new directory. New directory has inner keys as new keys and
    directories (with outer keys and inner values) as new values.
    EXAMPLE: outer_dir = {'A':{'a':1,'b':2}, 'B':{'a':2, 'c':5}}
    new_outer_dir = {'a':{'A':1,'B':2}, 'b':{'A':2, 'B':0}, 'c':{'A':0, 'B':5}}
    """
    outer_keys = []
    inner_keys = []
    for outer_key in directory.keys():
        outer_keys.append(outer_key)
        for inner_key in directory[outer_key].keys():
            if inner_key not in inner_keys:
                inner_keys.append(inner_key)
    new_outer_dir = {}
    for inner_key in inner_keys:
        new_inner_dir = {}
        for outer_key in outer_keys:
            if inner_key in directory[outer_key]:
                new_inner_dir[outer_key] = directory[outer_key][inner_key]
            else:
                new_inner_dir[outer_key] = 0
        new_outer_dir[inner_key] = new_inner_dir
    return new_outer_dir


dir = {'A':{'a':1,'b':2}, 'B':{'a':2, 'c':5}, 'C':{'a':4, 'b':3, 'c':2, 'd':4}}
print(dir)
print(inner_to_outer_dir(dir))