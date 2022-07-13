
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
#    print lst
    return max(lst, key=lst.count)[0]

def extract_value_with_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
#    print lst
    return min(lst, key=lst.count)[0]

def extract_value_with_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
#    print lst
    return max(lst, key=lst.count)[0]

def extract_value_with_avg(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the average of the values.
    """
#    print lst
    return sum(lst)/len(lst)

def extract_value_with_std(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the standard deviation of the values.
    """
#    print lst
    return math.sqrt(sum(lst)/len(lst))

def extract_value_with_median(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the median of the values.
    """
#    print lst
    return numpy.median(lst)

def extract_value_with_minmax(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest and the largest values.
    """
#    print lst
    return min(lst, key=lst.count)[0], max(lst, key=lst.count)[0]

def extract_value_with_minmax_with_median(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest and the largest values.
    """
#    print lst
    return numpy.median(lst), numpy.median