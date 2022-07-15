
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    return (b - a), (a * b), (a * a)


def make_tuple_of_tuples(l):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    return tuple(tuple(make_tuple(*i)) for i in l)


def make_tuple_of_tuples_of_tuples(l):
    """
    Given a list of lists of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    return tuple(tuple(make_tuple_of_tuples(i)) for i in l)


def make_tuple_of_tuples_of_tuples_of_tuples(l):
    """
    Given a list of lists of lists of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    return tuple(tuple(make_tuple_of_tuples_of_tuples(i)) for i in l)


def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples(l):
    """
    Given a list of lists of lists of lists of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    return tuple(tuple(make_tuple_of_tuples_of_tuples_of_tuples(i)) for i in l)


def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples(l):
    """
    Given a list of lists of lists of lists of lists of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    return tuple(tuple(make_tuple_of_tuples_of_tuples_of_tuples_of_tuples(i)) for i in l)


def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples(l):
    """
    Given a list of lists of lists of lists of lists of lists of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    return tuple(tuple(make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples(i)) for i in l)


def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples(l):
    """
    Given 