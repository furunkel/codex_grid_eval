
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
#    print(lst)
    return max(lst, key=lst.count)[0]

def find_max_value(lst):
    """
    Given a list of tuples, write a function that returns the largest value of the tuple with the smallest first value.
    """
#    print(lst)
    return max(lst, key=lst.count)[0]

def find_min_value(lst):
    """
    Given a list of tuples, write a function that returns the smallest value of the tuple with the smallest first value.
    """
#    print(lst)
    return min(lst, key=lst.count)[0]

def find_median_value(lst):
    """
    Given a list of tuples, write a function that returns the median value of the tuple with the smallest first value.
    """
#    print(lst)
    return median(lst, key=lst.count)[0]

def find_mode(lst):
    """
    Given a list of tuples, write a function that returns the mode of the tuple with the smallest first value.
    """
#    print(lst)
    return mode(lst, key=lst.count)[0]

def find_median_mode(lst):
    """
    Given a list of tuples, write a function that returns the median mode of the tuple with the smallest first value.
    """
#    print(lst)
    return median(lst, key=lst.count)[0]

def find_mode_median(lst):
    """
    Given a list of tuples, write a function that returns the median mode of the tuple with the smallest first value.
    """
#    print(lst)
    return mode(lst, key=lst.count)[0]

def find_mode_mode(lst):
    """
    Given a list of tuples, write a function that returns the mode of the tuple with the smallest first value.
    """
#    print(lst)
    return mode(lst, key=lst.count)[0]

def find_median_mode_median(lst):
    """
    Given a list of tuples, write a function that returns the median mode of the tuple with the smallest first value.