
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
#    print "tuple_extract", lst
    if len(lst) == 0:
        return None
    return tuple(lst[0])

def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
#    print "tuple_extract_with_min", lst
    if len(lst) == 0:
        return None
    return tuple(lst[0][0])

def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
#    print "tuple_extract_with_max", lst
    if len(lst) == 0:
        return None
    return tuple(lst[0][1])

def tuple_extract_with_min_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
#    print "tuple_extract_with_min_max", lst
    if len(lst) == 0:
        return None
    return tuple(lst[0][0])

def tuple_extract_with_max_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
#    print "tuple_extract_with_max_min", lst
    if len(lst) == 0:
        return None
    return tuple(lst[0][1])

def tuple_extract_with_min_max_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
#    print "tuple_extract_with_min_max_max", lst
    if len(lst) == 0:
        return None
    return tuple(lst[0][1])

def tuple_extract_with_max_min_max(lst):
    """
    Given a list of tuples, write