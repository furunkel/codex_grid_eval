
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest last value.
    """
#    print(lst)
    return max(lst, key=lst.count)

def find_max_value(lst):
    """
    Given a list of tuples, write a function that returns the largest value of the tuple with the largest value.
    """
    return max(lst, key=lst.count)

def find_min_value(lst):
    """
    Given a list of tuples, write a function that returns the smallest value of the tuple with the smallest value.
    """
    return min(lst, key=lst.count)

def find_median_value(lst):
    """
    Given a list of tuples, write a function that returns the median value of the tuple with the median value.
    """
    return median(lst, key=lst.count)

def find_variance(lst):
    """
    Given a list of tuples, write a function that returns the variance of the tuple with the variance.
    """
    return variance(lst, key=lst.count)

def find_variance_of_list(lst):
    """
    Given a list of tuples, write a function that returns the variance of the tuple with the variance of the list.
    """
    return variance(lst, key=lst.count)

def find_variance_of_list_of_lists(lst):
    """
    Given a list of tuples, write a function that returns the variance of the list of lists.
    """
    return variance(lst, key=lst.count)

def find_variance_of_list_of_lists_of_lists(lst):
    """
    Given a list of tuples, write a function that returns the variance of the list of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of lists of