
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
#    print lst
    return max(lst, key=lst.count)

def find_max_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest last value.
    """
#    print lst
    return max(lst, key=lst.count)

def find_min_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
#    print lst
    return min(lst, key=lst.count)

def find_median_value(lst):
    """
    Given a list of tuples, write a function that returns the median value of the tuple with the largest median value.
    """
#    print lst
    return median(lst, key=lst.count)

def find_mode(lst):
    """
    Given a list of tuples, write a function that returns the mode of the tuple with the largest mode.
    """
#    print lst
    return mode(lst, key=lst.count)

def find_median_mode(lst):
    """
    Given a list of tuples, write a function that returns the median mode of the tuple with the largest median mode.
    """
#    print lst
    return median(lst, key=lst.count)

def find_mode_median(lst):
    """
    Given a list of tuples, write a function that returns the median mode of the tuple with the largest median mode.
    """
#    print lst
    return mode(lst, key=lst.count, median=True)

def find_mode_mode(lst):
    """
    Given a list of tuples, write a function that returns the mode of the tuple with the largest mode.
    """
#    print lst
    return mode(lst, key=lst.count, median=True, mode='median')

def find_median_mode_median(lst):
    """
    Given a list of tuples, write a function that returns the median mode of the tuple with the largest median mode.
    """
#    print lst
    return median(lst, key=lst.count, median=True