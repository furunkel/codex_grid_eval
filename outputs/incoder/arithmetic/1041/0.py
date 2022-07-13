
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return (a-b, b*a, a+b)

def make_tuple_of_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return tuple([make_tuple(*i) for i in a])

def make_tuple_of_tuples_with_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return tuple([make_tuple_with_tuples(*i) for i in a])

def make_tuple_of_tuples_with_tuples_with_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return tuple([make_tuple_with_tuples_with_tuples(*i) for i in a])

def make_tuple_of_tuples_with_tuples_with_tuples_with_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return tuple([make_tuple_with_tuples_with_tuples_with_tuples(*i) for i in a])

def make_tuple_of_tuples_with_tuples_with_tuples_with_tuples_with_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return tuple([make_tuple_with_tuples_with_tuples_with_tuples_with_tuples(*i) for i in a])

def make_tuple_of_tuples_with_tuples_with_tuples_with_tuples_with_tuples_with_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return tuple([make_tuple_with_tuples_with_tuples_with_tuples_with_tuples_with_tuples(*i) for i in a])

def make_tuple_of_tuples_with_tuples_with_tuples_with_tuples_with_tuples_with_tuples_with_tuple