
def f(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lambda x: x[11])[11]

def g(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple.
    """
    return sum(x[1] for x in lst)

def h(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    but only if the second value is greater than the first value.
    """
    return sum(x[1] for x in lst if x[1] > x[0])

def i(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    but only if the second value is greater than the first value and the third value is greater than the second value.
    """
    return sum(x[1] for x in lst if x[1] > x[0] and x[2] > x[1])

def j(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    but only if the second value is greater than the first value and the third value is greater than the second value.
    """
    return sum(x[1] for x in lst if x[1] > x[0] and x[2] > x[1])

def k(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    but only if the second value is greater than the first value and the third value is greater than the second value.
    """
    return sum(x[1] for x in lst if x[1] > x[0] and x[2] > x[1])

def l(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    but only if the second value is greater than the first value and the third value is greater than the second value.
    """
    return sum(x[1