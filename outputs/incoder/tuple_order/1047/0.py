
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The second element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    """
    return (a*b, a-b, a+b)


def make_tuple_of_tuples(tuple_of_tuples):
    """
    Given a tuple of tuples, return a tuple of tuples where:
    The second element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    """
    return tuple([make_tuple(*tup) for tup in tuple_of_tuples])


def make_tuple_of_tuples_with_tuples(tuple_of_tuples):
    """
    Given a tuple of tuples, return a tuple of tuples where:
    The second element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    """
    return tuple([make_tuple_with_tuples(tup) for tup in tuple_of_tuples])


def make_tuple_of_tuples_with_tuples_of_tuples(tuple_of_tuples):
    """
    Given a tuple of tuples, return a tuple of tuples where:
    The second element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    """
    return tuple([make_tuple_with_tuples_of_tuples(tup) for tup in tuple_of_tuples])


def make_tuple_of_tuples_with_tuples_of_tuples_with_tuples(tuple_of_tuples):
    """
    Given a tuple of tuples, return a tuple of tuples where:
    The second element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    """
    return tuple([make_tuple_with_tuples_of_tuples_with_tuples(tup) for tup in tuple_of_tuples])


def make_tuple_of_tuples_with_tuples_of_tuples_with_tuples_with_tuples(tuple_of_tuples):
    """
    Given a tuple of tuples, return a tuple of tuples where:
    The second element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    """
    return tuple([make_tuple_with_tuples_of_tuples_with_tuples_with_tuples(tup) for tup in tuple_of_tuples])


def make_tuple_of_tuples_with_tuples_of_tuples_with_tuples_with_tuples_with_tuples(tuple_of_tuples):
    """
    Given a tuple of tuples, return a tuple of tuples where:
    The second element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    """
    return tuple([make_tuple_