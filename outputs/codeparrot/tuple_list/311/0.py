
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
#    print(lst)
    return max(lst, key=lst.count)

def min_max_by_key(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
#    print(lst)
    return max(lst, key=lst.count, reverse=True)

def min_max_by_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
#    print(lst)
    return max(lst, key=lst.count, reverse=True, key_func=lambda x: x[1])

def min_max_by_key_func(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
#    print(lst)
    return max(lst, key=lst.count, reverse=True, key_func=lambda x: x[1], reverse_func=lambda x: x[0])

def min_max_by_value_func(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
#    print(lst)
    return max(lst, key=lst.count, reverse=True, key_func=lambda x: x[1], reverse_func=lambda x: x[0], reverse_func_args=[1])

def min_max_by_key_func_args(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
#    print(lst)
    return max(lst, key=lst.count, reverse=True, key_func=lambda x: x[1], reverse_func_args=[1])

def min_max_by_key_func_args_by_value(lst):
    """
    Given a list of tuples, write a function that returns