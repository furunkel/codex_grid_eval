def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[1]


def fibonacci_with_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[1]


def fibonacci_with_min(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest third value.
    """
    return min(lst, key=lst.count)[1]


def fibonacci_with_avg(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the average of the values.
    """
    return sum(lst)/len(lst)


def fibonacci_with_std(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the standard deviation.
    """
    return math.sqrt(sum(lst))/len(lst)


def fibonacci_with_var(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the variance of the values.
    """
    return math.sqrt(sum(lst))/len(lst)


def fibonacci_with_skewness(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the skewness.
    """
    return math.sqrt(sum(lst))/len(lst)


def fibonacci_with_kurtosis(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the kurtosis.
    """
    return math.sqrt(sum(lst))/len(lst)


def fibonacci_with_skewness_kurtosis(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the