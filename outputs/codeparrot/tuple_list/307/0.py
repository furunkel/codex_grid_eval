
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
#    print "tuple_extract", lst
    return max(lst, key=lambda x: x[1])[1]

def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
#    print "tuple_extract_with_max", lst
    return max(lst, key=lambda x: x[1])[1]

def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
#    print "tuple_extract_with_min", lst
    return min(lst, key=lambda x: x[1])[1]

def tuple_extract_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the sum of the values.
    """
#    print "tuple_extract_with_sum", lst
    return sum(lst, key=lambda x: x[1])[1]

def tuple_extract_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the mean of the values.
    """
#    print "tuple_extract_with_mean", lst
    return mean(lst, key=lambda x: x[1])[1]

def tuple_extract_with_std(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the standard deviation of the values.
    """
#    print "tuple_extract_with_std", lst
    return std(lst, key=lambda x: x[1])[1]

def tuple_extract_with_var(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the variable.
    """
#    print "tuple_extract_with_var", lst
    return var(lst, key=lambda x: x[1])[1]
