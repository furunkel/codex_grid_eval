
def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
    return max(lst, key=lambda x: x[0])[1]


def g(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]


def h(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(lst, key=lambda x: x[1])[1]


def i(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[1]


def j(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest sum of values.
    """
    return max(lst, key=lambda x: x[0] + x[1])[1]


def k(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest sum of values.
    """
    return min(lst, key=lambda x: x[0] + x[1])[1]


def l(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest difference between
    values.
    """
    return max(lst, key=lambda x: abs(x[0] - x[1]))[1]


def m(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest difference between
    values.
    """
    return min(lst, key=lambda x: abs(x[0] - x[1]))[1]


def n(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest product of values.