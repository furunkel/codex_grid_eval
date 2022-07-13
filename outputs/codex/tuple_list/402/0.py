
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[11])[-1]


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
    Given a list of tuples, write a function that returns a dictionary with the first item as the key and the second item as the value.
    """
    return {x[0]: x[1] for x in lst}


def convert_to_dictionaries(lst):
    """
    Given a list of tuples, write a function that returns a list of dictionaries with the first item as the key and the second item as the value.
    """
    return [{x[0]: x[1]} for x in lst]


def convert_to_dictionaries_general(lst, n):
    """
    Given a list of tuples and an integer, write a function that returns a list of dictionaries with the first n items as the key and the last item as the value.
    """
    return [{x[i]: x[-1] for i in range(n)} for x in lst]


def convert_to_namedtuples(lst, name):
    """
    Given a list of tuples and a tuple name, write a function that returns a list of namedtuples with the first item as the key and the second item as the value.
    """
    return [namedtuple(name, x[0])(*x[1:]) for x in lst]


def convert_to_namedtuples_general(lst, name, n):
    """
    Given a list of tuples, a tuple name, and an integer, write a function that returns a list of namedtuples with the first n items as the key and the last