
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest third value.
    """
#    print lst
    return max(lst, key=lst.count)

def min_max_by_key(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest fourth value.
    """
#    print lst
    return max(lst, key=lst.count, reverse=True)

def min_max_by_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest fifth value.
    """
#    print lst
    return min(lst, key=lst.count, reverse=True)

def min_max_by_key_by_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest fifth value.
    """
#    print lst
    return min(lst, key=lst.count, reverse=True, key_by_value=True)

def min_max_by_key_by_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest fifth value.
    """
#    print lst
    return min(lst, key=lst.count, reverse=True, key_by_value=True, key_by_value_reverse=True)

def min_max_by_key_by_value_reverse(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest fifth value.
    """
#    print lst
    return min(lst, key=lst.count, reverse=True, key_by_value=True, key_by_value_reverse=True)

def min_max_by_key_by_value_reverse(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest fifth value.
    """
#    print lst
    return min(lst, key=lst.count, reverse=True, key_by_value=True, key_by