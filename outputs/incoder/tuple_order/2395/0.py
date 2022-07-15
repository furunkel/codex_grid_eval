
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    """
    return (a * b, b * a, a * a - b * b)


def make_tuple_of_tuples(b):
    """
    Given a list b, return a tuple where:
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    """
    return tuple(tuple(make_tuple(b, a)) for a, b in zip(b[:-1], b[1:]))


def make_tuple_of_tuples_of_tuples(b):
    """
    Given a list b, return a tuple where:
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    """
    return tuple(tuple(make_tuple_of_tuples(a)) for a, b in zip(b[:-1], b[1:]))


def make_tuple_of_tuples_of_tuples_of_tuples(b):
    """
    Given a list b, return a tuple where:
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    """
    return tuple(tuple(make_tuple_of_tuples_of_tuples(a)) for a, b in zip(b[:-1], b[1:]))


def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples(b):
    """
    Given a list b, return a tuple where:
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    """
    return tuple(tuple(make_tuple_of_tuples_of_tuples_of_tuples(a)) for a, b in zip(b[:-1], b[1:]))


def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples(b):
    """
    Given a list b, return a tuple where:
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    """
    return tuple(tuple(make_tuple_of_tuples_of_tuples_of_tuples_of_tuples(a)) for a, b in zip(b[:-1], b[1:]))


def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples(b):
    """
    Given a list b, return a tuple where:
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    """
    return tuple(tuple(make_tuple_of_tuples_of_tuples_of_tuples_of_tuples(a)) for a, b in zip(b[:-1], b[1:]))


def make_tuple_of_tuples_of_tuples_of_tuple