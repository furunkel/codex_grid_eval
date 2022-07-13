
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return (b - a), a * b + a, a + b


def make_tuple_of_tuples(l):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    tuple_of_tuples = []
    for tup in l:
        tuple_of_tuples.append(make_tuple(*tup))
    return tuple_of_tuples


def make_tuple_of_tuples_2(l):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    tuple_of_tuples = []
    for tup in l:
        tuple_of_tuples.append(make_tuple_2(*tup))
    return tuple_of_tuples


def make_tuple_of_tuples_3(l):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    tuple_of_tuples = []
    for tup in l:
        tuple_of_tuples.append(make_tuple_3(*tup))
    return tuple_of_tuples


def make_tuple_of_tuples_4(l):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    tuple_of_tuples = []
    for tup in l:
        tuple_of_tuples.append(make_tuple_4(*tup))
    return tuple_of_tuples


def make_tuple_of_tuples_5(l):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    tuple_of_tuples = []
    for tup in l:
        tuple_of_tuples.append(make_tuple_5(*tup))
    return tuple_of_tuples


def make_tuple_of_tuples_6(l):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    tuple_of_tuples = []
    for tup in l:
        tuple_of_tuples.append(make_tuple_6(*tup))
    return tuple_of_