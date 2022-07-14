def min_max(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[1])[0]


def min_max_by_key(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[1])[1]


def min_max_by_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[1])[1]


def min_max_by_key_and_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value and the second value.
    """
    return min(lst, key=lambda x: x[1], value=lambda x: x[0])


def min_max_by_key_and_value_and_key(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value and the second value and the third value.
    """
    return min(lst, key=lambda x: x[1], value=lambda x: x[0], key=lambda x: x[1], value=lambda x: x[0])


def min_max_by_key_and_value_and_key_and_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value and the second value and the third value.
    """
    return min(lst, key=lambda x: x[1], value=lambda x: x[0], key=lambda x: x[1], value=lambda x: x[0], key=lambda x: x[1], value=lambda x: x[0])


def min_max_by_key_and_value_and_key_and_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value and