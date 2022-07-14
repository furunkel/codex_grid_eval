def min_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lst.count)


def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lst.count, reverse=True)


def max_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return min(lst, key=lst.count, reverse=True)


def max_min_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return min(lst, key=lst.count, reverse=True, key=key)


def max_min_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return min(lst, key=lst.count, reverse=True, value=value)


def min_max_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lst.count, reverse=True, value=value)


def max_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lst.count, reverse=True, key=key)


def max_max_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lst.count, reverse=True, value=value)


def min_min_by_value(lst, value):
    """
    Given a list of