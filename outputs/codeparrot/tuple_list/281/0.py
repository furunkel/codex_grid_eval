
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
#    print(lst)
    return max(lst, key=lst.count)

def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return min(lst, key=lst.count, reverse=True)

def max_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return max(lst, key=lst.count, reverse=True)

def max_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count, reverse=True)

def max_min_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
    return min(lst, key=lst.count, reverse=True)

def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
    return min(lst, key=lst.count, reverse=True)

def max_min_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return max(lst, key=lst.count, reverse=True)

def max_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count, reverse=True)

def max_min_by_key(lst, key):
    """
    Given a list of tuples, write a