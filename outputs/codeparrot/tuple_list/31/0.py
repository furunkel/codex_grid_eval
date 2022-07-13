
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest third value.
    """
#    print(lst)
    return max(lst, key=lst.count)

def tuple_extract_with_max(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest third value.
    """
#    print(lst)
    return max(lst, key=lst.count)[-1]

def tuple_extract_with_min(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest third value.
    """
#    print(lst)
    return min(lst, key=lst.count)[-1]

def tuple_extract_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the sum of the values.
    """
#    print(lst)
    return sum(lst, key=lst.count)[-1]

def tuple_extract_with_count(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the count of the values.
    """
#    print(lst)
    return sum(lst, key=lst.count)[-1]

def tuple_extract_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the mean of the values.
    """
#    print(lst)
    return mean(lst, key=lst.count)[-1]

def tuple_extract_with_std(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the standard deviation of the values.
    """
#    print(lst)
    return std(lst, key=lst.count)[-1]

def tuple_extract_with_var(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the variance of the values.
    """
#    print(lst)
    return var(lst, key=lst.count)[-1]

def tuple_extract_with_median(lst):
    """
    Given