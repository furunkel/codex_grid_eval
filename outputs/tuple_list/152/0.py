
def f(text):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest first value.
    """
    return max(text, key=lambda x: x[0])[2]


def g(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[0]


def h(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest third value.
    """
    return max(text, key=lambda x: x[2])[1]


def i(text):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    return min(text, key=lambda x: x[0])[2]


def j(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[0]


def k(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
    return min(text, key=lambda x: x[2])[1]


def l(text):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the second largest first value.
    """
    return sorted(text, key=lambda x: x[0])[-2][2]


def m(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the second largest second value.
    """
    return sorted(text, key=lambda x: x[1])[-2][0]


def n(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the second largest third value.
    """
    return sorted(text, key=lambda x: x[2])[-2][1]


def o(text):
    """
    Given a list of tu