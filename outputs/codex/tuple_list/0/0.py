
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[0]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple.
    """
    return [x[0] for x in lst]


def remove_duplicates(lst):
    """
    Given a list of tuples, write a function that returns a list of tuples with duplicates removed.
    """
    return list(set(lst))


def swap_elements(lst):
    """
    Given a list of tuples, write a function that swaps the order of the elements in each tuple.
    """
    return [x[::-1] for x in lst]


def reverse_tuple(tup):
    """
    Given a tuple, write a function that reverses the order of the elements.
    """
    return tup[::-1]


def convert_list(lst):
    """
    Given a list of tuples, write a function that converts the list into a dictionary.
    """
    return {x[0]: x[1] for x in lst}


def convert_dictionary(dct):
    """
    Given a dictionary, write a function that converts the dictionary into a list of tuples.
    """
    return [(x, dct[x]) for x in dct]


def merge_dictionaries(dct1, dct2):
    """
    Given two dictionaries, write a function that merges the two dictionaries into a new dictionary.
    """
    return {**dct1, **dct2}


def invert_dictionary(dct):
    """
    Given a dictionary, write a function that inverts the keys and values of the dictionary.
    """
    return {v: k for k, v in dct.items()}


def count_characters(string):
    """
    Given a string, write a function that returns a dictionary containing each character and the number of times it appears.
    """
    return {x: string.count(x) for x in string}


def contains_