def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest eleventh value.
    """
    return max(lst, key=lst.count)[0]


def fibonacci_with_max(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lst.count)[0]


def fibonacci_with_min(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lst.count)[0]


def fibonacci_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the sum of the values.
    """
    return sum(lst, key=lst.count)[0]


def fibonacci_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the mean of the values.
    """
    return sum(lst, key=lst.count)[0]


def fibonacci_with_median(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the median of the values.
    """
    return median(lst, key=lst.count)[0]


def fibonacci_with_mode(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the mode of the tuple.
    """
    return mode(lst, key=lst.count)[0]


def fibonacci_with_mean_mode(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the mean of the values.
    """
    return mean(lst, key=lst.count)[0]


def fibonacci_with_mode_mean(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the mode of the tuple.
    """
    return mode