
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
#    print lst
    return max(lst, key=lst.count)

def find_max_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[-1]

def find_min_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(lst, key=lst.count)[-1]

def find_median_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the median second value.
    """
    return median(lst, key=lst.count)[-1]

def find_variance(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the variance second value.
    """
    return variance(lst, key=lst.count)[-1]

def find_skewness(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the skewness second value.
    """
    return skewness(lst, key=lst.count)[-1]

def find_kurtosis(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the kurtosis second value.
    """
    return kurtosis(lst, key=lst.count)[-1]

def find_standard_deviation(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the standard deviation second value.
    """
    return standard_deviation(lst, key=lst.count)[-1]

def find_skewness_deviation(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the skewness second value.
    """
    return skewness_deviation(lst, key=lst.count)[-1]

def find_kurtosis_deviation(lst):
    """
    Given a list of tuples, write