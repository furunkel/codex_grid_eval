def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
    return max(lst, key=lst.count)[1]


def fibonacci_with_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[1]


def fibonacci_with_min(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
    return min(lst, key=lst.count)[1]


def fibonacci_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the sum of the values.
    """
    return sum(lst, key=lst.count)[1]


def fibonacci_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the mean of the values.
    """
    return mean(lst, key=lst.count)[1]


def fibonacci_with_std(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the standard deviation of the values.
    """
    return std(lst, key=lst.count)[1]


def fibonacci_with_var(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the variance of the values.
    """
    return var(lst, key=lst.count)[1]


def fibonacci_with_median(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the median of the values.
    """
    return median(lst, key=lst.count)[1]


def fibonacci_with_mode(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the mode