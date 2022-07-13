
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
#    return max(lst, key=lst.count)
    return max(lst, key=lst.count)[0]

def min_max_by_key(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
#    return max(lst, key=lst.count)[0]
    return max(lst, key=lst.count)[0][0]

def min_max_by_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
#    return max(lst, key=lst.count)[0][1]
    return max(lst, key=lst.count)[0][1]

def min_max_by_key_by_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
#    return max(lst, key=lst.count)[0][0][1]
    return max(lst, key=lst.count)[0][0][1]

def min_max_by_value_by_key(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
#    return max(lst, key=lst.count)[0][1][0]
    return max(lst, key=lst.count)[0][1][0]

def min_max_by_key_by_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
#    return max(lst, key=lst.count)[0][1][1]
    return max(lst, key=lst.count)[0][1][1]

def min_max_by_key_by_value_by_key(lst):
    """
    Given a list of tuples, write a function that returns the second value of