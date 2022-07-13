
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
#    return max(lst, key=lst.count)
    return max(lst, key=lst.index)

def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lst.index, reverse=True)

def max_min_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lst.index, reverse=True)

def max_min_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lst.index, reverse=True, value=value)

def min_max_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lst.index, reverse=True, value=value)

def max_min_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lst.index, reverse=True, value=value)

def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lst.index, reverse=True, key=key)

def max_min_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lst.index, reverse