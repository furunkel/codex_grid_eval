
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
#    print(lst)
    return max(lst, key=lst.count)[1]

def find_max_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[0]

def find_min_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lst.count)[0]

def find_median_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the median second value.
    """
    return median(lst, key=lst.count)[0]

def find_mode(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the mode.
    """
    return mode(lst, key=lst.count)[0]

def find_median_mode(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the median second value.
    """
    return median(lst, key=lst.count)[0]

def find_mode_median(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the median second value.
    """
    return mode_median(lst, key=lst.count)[0]

def find_median_median(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the median second value.
    """
    return median_median(lst, key=lst.count)[0]

def find_mode_mode(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the mode.
    """
    return mode_mode(lst, key=lst.count)[0]

def find_median_mode_median(lst):
    """
    Given a list of tuples, write a function that returns the second value of