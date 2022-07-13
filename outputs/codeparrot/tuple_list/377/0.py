
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
#    return max(lst, key=lst.count)
    return max(lst, key=lst.index)

def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return max(lst, key=lst.index, reverse=True)

def max_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(lst, key=lst.index, reverse=True)

def max_min_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(lst, key=lst.index, reverse=True, key=key)

def max_min_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(lst, key=lst.index, reverse=True, value=value)

def max_min_by_value_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(lst, key=lst.index, reverse=True, value=key)

def max_min_by_value_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(lst, key=lst.index, reverse=True, value=key, key_reverse=True)

def max_min_by_value_by_key_reverse(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(lst, key=lst.index, reverse=True, key_reverse=True, key