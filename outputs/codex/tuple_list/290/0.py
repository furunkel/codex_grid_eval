
def f(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]

def g(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple.
    """
    return sum(x[1] for x in lst)

def h(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    but only if the second value is even.
    """
    return sum(x[1] for x in lst if x[1] % 2 == 0)

def i(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    but only if the second value is even and the first value is greater than 5.
    """
    return sum(x[1] for x in lst if x[1] % 2 == 0 and x[0] > 5)

def j(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    but only if the second value is even and the first value is greater than 5.
    """
    return sum(x[1] for x in lst if x[1] % 2 == 0 and x[0] > 5)

def k(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    but only if the second value is even and the first value is greater than 5.
    """
    return sum(x[1] for x in lst if x[1] % 2 == 0 and x[0] > 5)

def l(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    but only if the second value is even and the first value is greater than 5.
    """
    return sum(x[1] for x in lst if x[1] % 2 == 0 and x[0] > 5)

def m(lst):
    """
    Given