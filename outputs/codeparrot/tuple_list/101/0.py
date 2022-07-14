def min_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
    return max(lst, key=lst.count)[1]


def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
    return max(lst, key=lst.count)[1]


def max_min_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
    return min(lst, key=lst.count)[1]


def max_min_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
    return min(lst, key=lst.count)[1]


def min_max_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
    return max(lst, key=lst.count)[1]


def max_min_by_key_and_value(lst, key, value):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
    return min(lst, key=lst.count)[1]


def max_min_by_key_and_value_and_key(lst, key, value, key_index):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value and the key.
    """
    return min(lst, key=lst.count)[1]


def min_max_by_key_and_value_and_key(lst, key, value, key_index):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value and the key.
    """
    return max(lst, key=lst.count)[1]


def max_min_by_key_and_value_and_key_and_value(lst