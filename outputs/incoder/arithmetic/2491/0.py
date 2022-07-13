
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The second element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return (b + a, a * b, a - b)

def make_tuple_of_tuples(b):
    """
    Given a list b, return a tuple where:
    The second element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return tuple(tuple(make_tuple(b[0], b[1])) for b in b)

def make_tuple_of_tuples_with_tuples(b):
    """
    Given a list b, return a tuple where:
    The second element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return tuple(tuple(make_tuple_with_tuples(b[0], b[1])) for b in b)

def make_tuple_of_tuples_with_tuples_with_tuples(b):
    """
    Given a list b, return a tuple where:
    The second element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return tuple(tuple(make_tuple_with_tuples_with_tuples(b[0], b[1])) for b in b)

def make_tuple_of_tuples_with_tuples_with_tuples_with_tuples(b):
    """
    Given a list b, return a tuple where:
    The second element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return tuple(tuple(make_tuple_with_tuples_with_tuples_with_tuples_with_tuples(b[0], b[1])) for b in b)

def make_tuple_of_tuples_with_tuples_with_tuples_with_tuples_with_tuples(b):
    """
    Given a list b, return a tuple where:
    The second element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return tuple(tuple(make_tuple_with_tuples_with_tuples_with_tuples_with_tuples_with_tuples(b[0], b[1])) for b in b)

def make_tuple_of_tuples_with_tuples_with_tuples_with_tuples_with_tuples_with_tuples(b):
    """
    Given a list b, return a tuple where:
    The second element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return tuple(tuple(make_tuple_with_tuples_with_tuples_with_tuples_with_tuples_with_tuples_with_tuples(b[0], b[1]