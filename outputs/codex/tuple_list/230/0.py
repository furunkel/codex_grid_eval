
def f(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[2]

def g(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]

def h(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[0]

def i(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
    return min(lst, key=lambda x: x[2])[1]

def j(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[2]

def k(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest third value.
    """
    return min(lst, key=lambda x: x[2])[0]

def l(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[2]

def m(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest fourth value.
    """
    return min(lst, key=lambda x: x[3])[0]

def n(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[3]

def o(lst):
    """
