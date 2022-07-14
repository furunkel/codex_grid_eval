def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[1]


def fibonacci_with_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[-1]


def fibonacci_with_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(lst, key=lst.count)[1]


def fibonacci_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return sum(lst, key=lst.count)[-1]


def fibonacci_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return sum(lst, key=lst.count)[-1]


def fibonacci_with_std(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return math.sqrt(lst[0] ** 2 + lst[1] ** 2)


def fibonacci_with_median(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return math.median(lst)


def fibonacci_with_mode(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[-1]


def fibonacci_with_mode_with_median(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return math.median(lst, key=lst.count)[-1