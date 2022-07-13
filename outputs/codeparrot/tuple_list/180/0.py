
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest twelfth value.
    """
#    print "extract_value"
    return max(lst, key=lambda x: x[1])[1]

def extract_value_with_min(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest twelfth value.
    """
#    print "extract_value_with_min"
    return min(lst, key=lambda x: x[1])[1]

def extract_value_with_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest twelfth value.
    """
#    print "extract_value_with_max"
    return max(lst, key=lambda x: x[1])[1]

def extract_value_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the mean twelfth value.
    """
#    print "extract_value_with_mean"
    return mean(lst, key=lambda x: x[1])[1]

def extract_value_with_median(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the median twelfth value.
    """
#    print "extract_value_with_median"
    return median(lst, key=lambda x: x[1])[1]

def extract_value_with_mode(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the mode of the tuple.
    """
#    print "extract_value_with_mode"
    return mode(lst, key=lambda x: x[1])[1]

def extract_value_with_mean_mode(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the mean mode of the tuple.
    """
#    print "extract_value_with_mean_mode"
    return mean_mode(lst, key=lambda x: x[1])[1]