
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest third value.
    """
#    return max(lst, key=lst.count)
    return max(lst, key=lst.count)[0]

def min_max_by_key(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest fourth value.
    """
#    return max(lst, key=lst.count)[1]
    return max(lst, key=lst.count)[2]

def min_max_by_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest fifth value.
    """
#    return max(lst, key=lst.count)[3]
    return max(lst, key=lst.count)[4]

def min_max_by_key_and_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest fifth value and the fifth value.
    """
#    return max(lst, key=lst.count)[5]
    return max(lst, key=lst.count)[6]

def min_max_by_value_and_key(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest fifth value and the fifth value.
    """
#    return max(lst, key=lst.count)[7]
    return max(lst, key=lst.count)[8]

def min_max_by_key_and_value_and_key(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest fifth value and the fifth value.
    """
#    return max(lst, key=lst.count)[9]
    return max(lst, key=lst.count)[10]

def min_max_by_key_and_value_and_key(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest fifth value and the fifth