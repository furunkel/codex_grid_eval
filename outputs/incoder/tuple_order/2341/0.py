
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The first element contains the product of the two numbers.
    The second element contains the sum of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return (b*a, a+b, a-b)

def make_tuple_of_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the product of the two numbers.
    The second element contains the sum of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return tuple([make_tuple(*a) for a in a])

def make_tuple_of_tuples_of_tuples(a):
    """
    Given a list of lists of tuples, return a tuple where:
    The first element contains the product of the two numbers.
    The second element contains the sum of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return tuple([make_tuple_of_tuples(a) for a in a])

def make_tuple_of_tuples_of_tuples_of_tuples(a):
    """
    Given a list of lists of lists of tuples, return a tuple where:
    The first element contains the product of the two numbers.
    The second element contains the sum of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return tuple([make_tuple_of_tuples_of_tuples(a) for a in a])

def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples(a):
    """
    Given a list of lists of lists of lists of tuples, return a tuple where:
    The first element contains the product of the two numbers.
    The second element contains the sum of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return tuple([make_tuple_of_tuples_of_tuples_of_tuples(a) for a in a])

def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples(a):
    """
    Given a list of lists of lists of lists of lists of tuples, return a tuple where:
    The first element contains the product of the two numbers.
    The second element contains the sum of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return tuple([make_tuple_of_tuples_of_tuples_of_tuples(a) for a in a])

def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples(a):
    """
    Given a list of lists of lists of lists of lists of tuples, return a tuple where:
    The first element contains the product of the two numbers.
    The second element contains the sum of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return tuple([make_tuple_of_tuples_of_tuples_of_tuples(a) for a in a])

def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples(a):
    """
    Given a list of lists of lists of lists of lists of tuples, return a tuple where:
    The first element contains the 