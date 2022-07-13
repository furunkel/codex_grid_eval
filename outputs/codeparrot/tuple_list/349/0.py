
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest last value.
    """
#    print "tuple_extract", lst
    return max(lst, key=lambda x: x[1])[0]

def tuple_extract_last(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
#    print "tuple_extract_last", lst
    return max(lst, key=lambda x: x[0])[0]

def tuple_extract_first(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
#    print "tuple_extract_first", lst
    return min(lst, key=lambda x: x[0])[0]

def tuple_extract_last_first(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
#    print "tuple_extract_last_first", lst
    return max(lst, key=lambda x: x[0])[0]

def tuple_extract_first_last(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
#    print "tuple_extract_first_last", lst
    return min(lst, key=lambda x: x[0])[0]

def tuple_extract_last_last(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest last value.
    """
#    print "tuple_extract_last_last", lst
    return max(lst, key=lambda x: x[0])[0]

def tuple_extract_first_last_last(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest last value.
    """
#    print "tuple_extract_first_last_last", lst
    return min(lst, key=lambda x: x[0])[0]

def tuple_extract_