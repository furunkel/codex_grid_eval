
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
#    print "tuple_extract", lst
    if len(lst) == 0:
        return None
    return max(lst, key=lambda x: x[1])[1]

def tuple_extract_with_last(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
#    print "tuple_extract_with_last", lst
    if len(lst) == 0:
        return None
    return max(lst, key=lambda x: x[1])[1]

def tuple_extract_with_first(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
#    print "tuple_extract_with_first", lst
    if len(lst) == 0:
        return None
    return max(lst, key=lambda x: x[1])[1]

def tuple_extract_with_last_with_first(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
#    print "tuple_extract_with_last_with_first", lst
    if len(lst) == 0:
        return None
    return max(lst, key=lambda x: x[1])[1]

def tuple_extract_with_first_with_last(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
#    print "tuple_extract_with_first_with_last", lst
    if len(lst) == 0:
        return None
    return max(lst, key=lambda x: x[1])[1]

def tuple_extract_with_last_with_first_with_last(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
#    print "tuple_extract_with_last_with_first_with