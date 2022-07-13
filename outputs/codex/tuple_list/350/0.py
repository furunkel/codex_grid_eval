
def f(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest last value.
    """
    return min(lst, key=lambda x: x[-1])[-2]

def g(lst):
    """
    Given a list of tuples, write a function that returns the sum of the last two values of the tuple with the smallest last value.
    """
    return sum(min(lst, key=lambda x: x[-1])[-2:])

def h(lst):
    """
    Given a list of tuples, write a function that returns the sum of the last two values of the tuple with the smallest sum of the last two values.
    """
    return sum(min(lst, key=lambda x: sum(x[-2:]))[-2:])

def i(lst):
    """
    Given a list of tuples, write a function that returns the sum of the last two values of the tuple with the smallest sum of the last two values.
    """
    return sum(min(lst, key=lambda x: sum(x[-2:]))[-2:])

def j(lst):
    """
    Given a list of tuples, write a function that returns the sum of the last two values of the tuple with the smallest sum of the last two values.
    """
    return sum(min(lst, key=lambda x: sum(x[-2:]))[-2:])

def k(lst):
    """
    Given a list of tuples, write a function that returns the sum of the last two values of the tuple with the smallest sum of the last two values.
    """
    return sum(min(lst, key=lambda x: sum(x[-2:]))[-2:])

def l(lst):
    """
    Given a list of tuples, write a function that returns the sum of the last two values of the tuple with the smallest sum of the last two values.
    """
    return sum(min(lst, key=lambda x: sum(x[-2:]))[-2:])

def m(lst):
    """
    Given a list of tuples, write a function that returns the sum of the last two values of the tuple with the smallest sum of the