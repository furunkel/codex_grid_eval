
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
#    print lst
    return max(lst, key=lst.count)

def fibonacci_with_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lst.count)

def fibonacci_with_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lst.count)

def fibonacci_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the mean twelfth value.
    """
    return mean(lst, key=lst.count)

def fibonacci_with_median(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the median twelfth value.
    """
    return median(lst, key=lst.count)

def fibonacci_with_std(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the standard deviation twelfth value.
    """
    return std(lst, key=lst.count)

def fibonacci_with_var(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the variable twelfth value.
    """
    return var(lst, key=lst.count)

def fibonacci_with_skewness(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the skewness twelfth value.
    """
    return skewness(lst, key=lst.count)

def fibonacci_with_kurtosis(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the kurtosis twelfth