def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
    return max(lst, key=lst.count)[0]


def fibonacci_with_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
    return max(lst, key=lst.count)[0]


def fibonacci_with_min(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
    return min(lst, key=lst.count)[0]


def fibonacci_with_average(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the average of the values.
    """
    return sum(lst)/len(lst)


def fibonacci_with_variance(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the variance of the values.
    """
    return sum(lst)/len(lst)


def fibonacci_with_standard_deviation(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the standard deviation of the values.
    """
    return math.sqrt(sum(lst)/len(lst))


def fibonacci_with_variance_deviation(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the variance of the values.
    """
    return math.sqrt(sum(lst)/len(lst))


def fibonacci_with_standard_deviation_deviation(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the standard deviation of the values.
    """
    return math.sqrt(sum(lst)/len(lst))


def fibonacci_with_variance_standard_deviation(lst):
    """
    Given a list of tuples, write a function that returns the