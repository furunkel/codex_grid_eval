
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
#    return min(lst, key=lambda x: x[1])[0]
    return max(lst, key=lambda x: x[1])[0]

def min_max_by_key(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
#    return min(lst, key=lambda x: x[1])[1]
    return max(lst, key=lambda x: x[1])[1]

def min_max_by_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
#    return min(lst, key=lambda x: x[1])[1]
    return max(lst, key=lambda x: x[1])[1]

def max_min(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
#    return max(lst, key=lambda x: x[1])[1]
    return min(lst, key=lambda x: x[1])[1]

def max_max_by_key(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
#    return max(lst, key=lambda x: x[1])[1]
    return max(lst, key=lambda x: x[1])[1]

def max_max_by_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
#    return max(lst, key=lambda x: x[1])[1]
    return max(lst, key=lambda x: x[1])[1]

def max_min_by_key(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
#    return