
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
#    print(lst)
    return max(lst, key=lambda x: x[1])[1]

def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
#    print(lst)
    return min(lst, key=lambda x: x[1])[1]

def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
#    print(lst)
    return max(lst, key=lambda x: x[1])[1]

def tuple_extract_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the sum of the values.
    """
#    print(lst)
    return sum(lst, key=lambda x: x[1])[1]

def tuple_extract_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the mean of the values.
    """
#    print(lst)
    return mean(lst, key=lambda x: x[1])[1]

def tuple_extract_with_median(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the median of the values.
    """
#    print(lst)
    return median(lst, key=lambda x: x[1])[1]

def tuple_extract_with_std(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the standard deviation of the values.
    """
#    print(lst)
    return std(lst, key=lambda x: x[1])[1]

def tuple_extract_with_var(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the variance of the values.
   