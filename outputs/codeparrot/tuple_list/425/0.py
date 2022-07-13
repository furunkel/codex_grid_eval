
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
#    return max(lst, key=lst.count)
    return max(lst, key=lst.index)

def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
    return max(lst, key=lst.index, reverse=True)

def max_min_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
    return min(lst, key=lst.index, reverse=True)

def max_min_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
    return max(lst, key=lst.index, reverse=True, value=value)

def max_min_by_value_by_key(lst, key, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
    return min(lst, key=lst.index, reverse=True, value=value, key_func=lambda x: x[1])

def max_min_by_value_by_key(lst, key, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
    return min(lst, key=lst.index, reverse=True, value=value, key_func=lambda x: x[1], reverse_func=lambda x: x[0])

def min_max_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
    return max(lst, key=lst.index, reverse=True, value=value, key_func=lambda x: x[1], reverse_func=lambda x: x[0])

def max_max_by_value(lst,