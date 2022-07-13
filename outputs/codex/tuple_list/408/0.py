
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lambda x: x[11])[-1]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of values in the order they appear in the tuples.
    """
    return [x[-1] for x in lst]


def remove_duplicates(lst):
    """
    Given a list of tuples, write a function that returns a list of tuples with duplicates removed.
    """
    return list(set(lst))


def convert_to_dictionary(lst):
    """
    Given a list of tuples, write a function that returns a dictionary with the first item in each tuple as the key and the second item as the value.
    """
    return {x[0]: x[1] for x in lst}


def convert_to_dictionary_of_lists(lst):
    """
    Given a list of tuples, write a function that returns a dictionary with the first item in each tuple as the key and the second item as the value.
    """
    return {x[0]: [x[1]] for x in lst}


def convert_to_dictionary_of_lists_v2(lst):
    """
    Given a list of tuples, write a function that returns a dictionary with the first item in each tuple as the key and the second item as the value.
    """
    d = {}
    for x in lst:
        if x[0] in d:
            d[x[0]].append(x[1])
        else:
            d[x[0]] = [x[1]]
    return d


def convert_to_dictionary_of_lists_v3(lst):
    """
    Given a list of tuples, write a function that returns a dictionary with the first item in each tuple as the key and the second item as the value.
    """
    d = {}
    for x in lst:
        d.setdefault(x[0], []).append(x[1])
    return d


def convert_to_dictionary_of_lists_v4(