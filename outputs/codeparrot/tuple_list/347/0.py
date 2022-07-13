
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
#    print(lst)
    return max(lst, key=lst.count)

def min_max_by_key(lst, key):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lst.count, reverse=True)

def min_max_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return min(lst, key=lst.count, reverse=True, key=value)

def min_max_by_key_by_value(lst, key, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return min(lst, key=lst.count, reverse=True, key=value, key_func=lambda x: x[1])

def min_max_by_key_by_value_by_key(lst, key, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return min(lst, key=lst.count, reverse=True, key=value, key_func=lambda x: x[1], reverse_func=lambda x: x[0])

def min_max_by_key_by_value_by_key(lst, key, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return min(lst, key=lst.count, reverse=True, key=value, key_func=lambda x: x[1], reverse_func=lambda x: x[0], reverse_func=lambda x: x[1])

def min_max_by_key_by_value_by_key(lst, key, value):
    """
    Given a