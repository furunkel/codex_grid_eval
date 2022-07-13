
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest eleventh value.
    """
#    print(lst)
    return max(lst, key=lst.count)

def find_max_value(lst):
    """
    Given a list of tuples, write a function that returns the largest value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lst.count)

def find_min_value(lst):
    """
    Given a list of tuples, write a function that returns the smallest value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lst.count)

def find_median_value(lst):
    """
    Given a list of tuples, write a function that returns the median value of the tuple with the median eleventh value.
    """
    return median(lst, key=lst.count)

def find_variance(lst):
    """
    Given a list of tuples, write a function that returns the variance of the tuple with the variance of the tuple.
    """
    return variance(lst, key=lst.count)

def find_skewness(lst):
    """
    Given a list of tuples, write a function that returns the skewness of the tuple with the skewness of the tuple.
    """
    return skewness(lst, key=lst.count)

def find_kurtosis(lst):
    """
    Given a list of tuples, write a function that returns the kurtosis of the tuple with the kurtosis of the tuple.
    """
    return kurtosis(lst, key=lst.count)

def find_standard_deviation(lst):
    """
    Given a list of tuples, write a function that returns the standard deviation of the tuple with the standard deviation of the tuple.
    """
    return standard_deviation(lst, key=lst.count)

def find_variance_deviation(lst):
    """
    Given a list of tuples, write a function that returns the variance of the tuple with the variance of the tuple.
    """
    return variance_deviation(lst, key=lst.count)

def find_skewness_deviation(lst):
    """
    Given a list of tuples, write a function that returns the skew