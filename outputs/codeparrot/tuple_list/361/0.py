
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
#    print(lst)
    return max(lst, key=lst.count)[0]

def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
#    print(lst)
    return min(lst, key=lst.count)[0]

def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest first value.
    """
#    print(lst)
    return max(lst, key=lst.count)[0]

def tuple_extract_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the sum of the values of the tuple with the smallest first value.
    """
#    print(lst)
    return sum(lst, key=lst.count)[0]

def tuple_extract_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the mean of the tuple with the smallest first value.
    """
#    print(lst)
    return mean(lst, key=lst.count)[0]

def tuple_extract_with_median(lst):
    """
    Given a list of tuples, write a function that returns the median of the tuple with the smallest first value.
    """
#    print(lst)
    return median(lst, key=lst.count)[0]

def tuple_extract_with_mode(lst):
    """
    Given a list of tuples, write a function that returns the mode of the tuple with the smallest first value.
    """
#    print(lst)
    return mode(lst, key=lst.count)[0]

def tuple_extract_with_mode_with_min(lst):
    """
    Given a list of tuples, write a function that returns the mode of the tuple with the smallest first value.
    """
#    print(lst)
    return mode(lst, key=lst.count)[0]

def tuple_extract_with_mode_with_max(lst):
    """