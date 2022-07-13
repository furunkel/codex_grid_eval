
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
#    if len(lst) == 0:
#        return 0
#    return max(lst, key=lst.count)
    return max(lst, key=lst.count)[0]

def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
#    if len(lst) == 0:
#        return 0
#    return max(lst, key=lst.count)[0]
    return max(lst, key=lst.count)[0][0]

def min_max_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
#    if len(lst) == 0:
#        return 0
#    return max(lst, key=lst.count)[0][1]
    return max(lst, key=lst.count)[0][1]

def min_max_by_key_by_value(lst, key, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
#    if len(lst) == 0:
#        return 0
#    return max(lst, key=lst.count)[0][1][key]
    return max(lst, key=lst.count)[0][1][key]

def min_max_by_value_by_key(lst, key, value):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
#    if len(lst) == 0:
#        return 0
#    return max(lst, key=lst.count)[0][1][key]
    return max(lst, key=lst.count)[0][1][key]

def min_max_by_key_by_value_by_key(lst, key, value):
    """