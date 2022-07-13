
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest last value.
    """
#    print "tuple_extract"
    return tuple(lst[0])

def tuple_extract_with_last(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest first value.
    """
#    print "tuple_extract_with_last"
    return tuple(lst[-1])

def tuple_extract_with_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
#    print "tuple_extract_with_first"
    return tuple(lst[0][0])

def tuple_extract_with_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest first value and the second value.
    """
#    print "tuple_extract_with_last_and_first"
    return tuple(lst[-1][0]), lst[-1][1]

def tuple_extract_with_first_and_last(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value and the second value.
    """
#    print "tuple_extract_with_first_and_last"
    return tuple(lst[0][0]), lst[0][1], lst[0][2]

def tuple_extract_with_last_and_first_and_last(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest first value and the second value.
    """
#    print "tuple_extract_with_last_and_first_and_last"
    return tuple(lst[-1][0]), lst[-1][1], lst[-1][2]

def tuple_extract_with_first_and_last_and_first(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value and the second value.
    """
#    print "tuple_extract_with_first_and