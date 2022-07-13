
def f(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[11])[0]

def g(lst):
    """
    Given a list of tuples, write a function that returns the sum of the last value of each tuple.
    """
    return sum(x[-1] for x in lst)

def h(lst):
    """
    Given a list of tuples, write a function that returns the sum of the second-to-last value of each tuple.
    """
    return sum(x[-2] for x in lst)

def i(lst):
    """
    Given a list of tuples, write a function that returns the sum of the third-to-last value of each tuple.
    """
    return sum(x[-3] for x in lst)

def j(lst):
    """
    Given a list of tuples, write a function that returns the sum of the fourth-to-last value of each tuple.
    """
    return sum(x[-4] for x in lst)

def k(lst):
    """
    Given a list of tuples, write a function that returns the sum of the fifth-to-last value of each tuple.
    """
    return sum(x[-5] for x in lst)

def l(lst):
    """
    Given a list of tuples, write a function that returns the sum of the sixth-to-last value of each tuple.
    """
    return sum(x[-6] for x in lst)

def m(lst):
    """
    Given a list of tuples, write a function that returns the sum of the seventh-to-last value of each tuple.
    """
    return sum(x[-7] for x in lst)

def n(lst):
    """
    Given a list of tuples, write a function that returns the sum of the eighth-to-last value of each tuple.
    """
    return sum(x[-8] for x in lst)

def o(lst):
    """
    Given a list of tuples, write a function that returns the sum of the ninth-to