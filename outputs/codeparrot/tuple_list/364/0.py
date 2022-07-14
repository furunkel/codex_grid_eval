def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    return max(lst, key=lst.count)[0]


def fibonacci_with_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest first value.
    """
    return max(lst, key=lst.count)[0]


def fibonacci_with_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    return min(lst, key=lst.count)[0]


def fibonacci_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the sum of the values.
    """
    return sum(lst, key=lst.count)[0]


def fibonacci_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the mean of the values.
    """
    return sum(lst, key=lst.count)[0]


def fibonacci_with_std(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the standard deviation of the values.
    """
    return math.sqrt(sum(lst, key=lst.count)[0])


def fibonacci_with_var(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the variance of the values.
    """
    return math.sqrt(sum(lst, key=lst.count)[0] / len(lst))


def fibonacci_with_median(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the median of the values.
    """
    return math.median(lst, key=lst.count)[0]


def fibonacci_with_mode(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the mode of the values