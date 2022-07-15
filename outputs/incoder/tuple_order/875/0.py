
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return (a-b, b+a, a*b)


def make_tuple_of_tuples(*args):
    """
    Given any number of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return tuple([make_tuple(*args) for args in zip(*args)])


def make_tuple_of_tuples_of_tuples(*args):
    """
    Given any number of tuples of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return tuple([make_tuple_of_tuples(*args) for args in zip(*args)])


def make_tuple_of_tuples_of_tuples_of_tuples(*args):
    """
    Given any number of tuples of tuples of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return tuple([make_tuple_of_tuples_of_tuples(*args) for args in zip(*args)])


def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples(*args):
    """
    Given any number of tuples of tuples of tuples of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return tuple([make_tuple_of_tuples_of_tuples_of_tuples(*args) for args in zip(*args)])


def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples(*args):
    """
    Given any number of tuples of tuples of tuples of tuples of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return tuple([make_tuple_of_tuples_of_tuples_of_tuples_of_tuples(*args) for args in zip(*args)])


def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples(*args):
    """
    Given any number of tuples of tuples of tuples of tuples of tuples of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return tuple([make_tuple_of_tuples_of_tuples_of_tuples_of_tuples(*args) for args in zip(*