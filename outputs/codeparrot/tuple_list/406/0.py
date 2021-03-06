def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lst.count)


def fibonacci_with_max_twelfth(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lst.count)[-1]


def fibonacci_with_min_twelfth(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lst.count)[-1]


def fibonacci_with_max_twelfth_and_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value and the smallest twelfth value.
    """
    return max(lst, key=lst.count)[-1], min(lst, key=lst.count)[-1]


def fibonacci_with_min_twelfth_and_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value and the largest twelfth value.
    """
    return min(lst, key=lst.count)[-1], max(lst, key=lst.count)[-1]


def fibonacci_with_max_twelfth_and_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value and the smallest twelfth value.
    """
    return max(lst, key=lst.count)[-1], min(lst, key=lst.count)[-1]


def fibonacci_with_min_twelfth_and_max_and_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value and the smallest twelfth