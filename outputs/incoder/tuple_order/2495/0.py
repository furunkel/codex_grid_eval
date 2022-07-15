
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return (b - a), sum(b), a * b


def make_tuple_of_tuples(b):
    """
    Given a list, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return tuple(map(make_tuple, b))


def make_tuple_of_tuples_with_tuples(b):
    """
    Given a list, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return tuple(map(make_tuple_of_tuples, b))


def make_tuple_of_tuples_with_different_lengths(b):
    """
    Given a list, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return tuple(map(make_tuple_of_tuples_with_different_lengths, b))


def make_tuple_of_tuples_with_different_lengths_and_different_types(b):
    """
    Given a list, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return tuple(map(make_tuple_of_tuples_with_different_lengths_and_different_types, b))


def make_tuple_of_tuples_with_different_lengths_and_different_types(b):
    """
    Given a list, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return tuple(map(make_tuple_of_tuples_with_different_lengths_and_different_types, b))


def make_tuple_of_tuples_with_different_lengths_and_different_types_2(b):
    """
    Given a list, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return tuple(map(make_tuple_of_tuples_with_different_lengths_and_different_types_2, b))


def make_tuple_of_tuples_with_different_lengths_and_different_types_3(b):
    """
    Given a list, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
