
def f(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest first value.
    """
    return max(lst, key=lambda x: x[0])[1]


def g(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]


def h(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(lst, key=lambda x: x[1])[1]


def i(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[1]


def j(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x: x[2])[1]


def k(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return min(lst, key=lambda x: x[2])[1]


def l(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest fourth value.
    """
    return max(lst, key=lambda x: x[3])[1]


def m(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest fourth value.
    """
    return min(lst, key=lambda x: x[3])[1]


def n(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest fifth value.
    """
    return max(lst, key=lambda x: x[4])[1]


def o(lst):
    """
