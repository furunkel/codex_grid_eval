
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest eleventh value.
    """
#    return max(lst, key=lst.count)
    return max(lst, key=lst.count)[0]

def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest eleventh value.
    """
#    return max(lst, key=lst.count)[0]
    return max(lst, key=lst.count)[0][0]

def max_min_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest eleventh value.
    """
#    return min(lst, key=lst.count)[0]
    return min(lst, key=lst.count)[0][1]

def max_min_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest eleventh value.
    """
#    return min(lst, key=lst.count)[0]
    return min(lst, key=lst.count)[0][1]

def max_min_by_value_by_key(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest eleventh value.
    """
#    return min(lst, key=lst.count)[0]
    return min(lst, key=lst.count)[0][1]

def max_min_by_value_by_key(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest eleventh value.
    """
#    return min(lst, key=lst.count)[0]
    return min(lst, key=lst.count)[0][1]

def min_max_by_key_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest eleventh value.
    """
#    return