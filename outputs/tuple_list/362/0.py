
def f(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    return min(text, key=lambda x: x[0])[1]


def g(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest first value.
    """
    return max(text, key=lambda x: x[0])[1]


def h(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[1]


def i(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[1]


def j(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return min(text, key=lambda x: x[2])[1]


def k(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(text, key=lambda x: x[2])[1]


def l(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest fourth value.
    """
    return min(text, key=lambda x: x[3])[1]


def m(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest fourth value.
    """
    return max(text, key=lambda x: x[3])[1]


def n(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest fifth value.
    """
    return min(text, key=lambda x: x[4])[1]


def o(text):
    """
    Given a list of tuples, write a function that returns the last value of the