
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
#    return max(lst, key=lst.count)
    return max(lst, key=lst.count)[0]

def min_max_by_key(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
#    return max(lst, key=lst.count)[0]
    return max(lst, key=lst.count)[0][0]

def min_max_by_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
#    return max(lst, key=lst.count)[0][1]
    return max(lst, key=lst.count)[0][1]

def min_max_by_key_and_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
#    return max(lst, key=lst.count)[0][1][0]
    return max(lst, key=lst.count)[0][1][0]

def min_max_by_key_and_value_and_key(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value and the key.
    """
#    return max(lst, key=lst.count)[0][1][1]
    return max(lst, key=lst.count)[0][1][1]

def min_max_by_key_and_value_and_key_and_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value and the key and value.
    """
#    return max(lst, key=lst.count)[0][1][1][0]
    return max(lst, key=lst.count)[0][1][1][0]

def min_max_by_key_and_value_