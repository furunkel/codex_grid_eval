
def f(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lambda x: x[10])[10]

def g(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[10])[10]

def h(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the second smallest eleventh value.
    """
    return sorted(lst, key=lambda x: x[10])[1][10]

def i(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the second largest eleventh value.
    """
    return sorted(lst, key=lambda x: x[10])[-2][10]

def j(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the third smallest eleventh value.
    """
    return sorted(lst, key=lambda x: x[10])[2][10]

def k(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the third largest eleventh value.
    """
    return sorted(lst, key=lambda x: x[10])[-3][10]

def l(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the fourth smallest eleventh value.
    """
    return sorted(lst, key=lambda x: x[10])[3][10]

def m(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the fourth largest eleventh value.
    """
    return sorted(lst, key=lambda x: x[10])[-4][10]

def n(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the fifth smallest ele