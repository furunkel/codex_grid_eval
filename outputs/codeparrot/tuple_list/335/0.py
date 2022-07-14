def min_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lst.count)


def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lst.count, reverse=True)


def max_min(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    return min(lst, key=lst.count, reverse=True)


def max_min_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    return min(lst, key=lst.count, reverse=True, key=key)


def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lst.count, reverse=True, key=key)


def max_min_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    return min(lst, key=lst.count, reverse=True, key=key)


def max_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lst.count, reverse=True, key=key)


def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    return min(lst, key=lst.count, reverse=True, key=