def min_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lst[-1])[1]


def min_max_by_key(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest value.
    """
    return min(lst, key=lst[0])[0]


def max_min_by_key(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the largest first value.
    """
    return min(lst, key=lst[-1])[1]


def max_min_by_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest value.
    """
    return max(lst, key=lst[0])[0]


def min_max_by_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest value.
    """
    return min(lst, key=lst[0])[1]


def max_max_by_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the largest last value.
    """
    return max(lst, key=lst[-1])[0]


def min_min_by_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest value.
    """
    return min(lst, key=lst[0])[0]


def max_min_by_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the largest first value.
    """
    return max(lst, key=lst[-1])[0]


def min_max_by_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest value.
    """
    return min(lst, key=lst[0])[1]


def max_max_by_value(lst):
    """
    Given a list of