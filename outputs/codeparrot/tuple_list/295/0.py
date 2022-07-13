
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
#    print "tuple_extract", lst
    return max(lst, key=lambda x: x[1])[0]

def tuple_extract_with_last(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
#    print "tuple_extract_with_last", lst
    return max(lst, key=lambda x: x[1])[0]

def tuple_extract_with_first(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
#    print "tuple_extract_with_first", lst
    return min(lst, key=lambda x: x[1])[0]

def tuple_extract_with_last_with_first(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
#    print "tuple_extract_with_last_with_first", lst
    return max(lst, key=lambda x: x[1])[0]

def tuple_extract_with_first_with_last(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
#    print "tuple_extract_with_first_with_last", lst
    return min(lst, key=lambda x: x[1])[0]

def tuple_extract_with_last_with_first_with_last(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
#    print "tuple_extract_with_last_with_first_with_last", lst
    return max(lst, key=lambda x: x[1])[0]

def tuple_extract_with_first_with_last_with_first(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the