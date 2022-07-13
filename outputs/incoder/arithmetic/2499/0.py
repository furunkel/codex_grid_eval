
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return (b - a), a * b + a, a + b


def make_tuple_of_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return tuple([tuple([x[0] - x[1] for x in a]), sum([x[0] * x[1] for x in a]), sum([x[1] + x[1] for x in a])])


def make_tuple_of_tuples_with_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return tuple([tuple([x[0] - x[1] for x in a]), tuple([x[0] * x[1] for x in a]), sum([x[1] + x[1] for x in a])])


def make_tuple_of_tuples_with_tuples_with_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return tuple([tuple([x[0] - x[1] for x in a]), tuple([x[0] * x[1] for x in a]), sum([x[1] + x[1] for x in a])])


def make_tuple_of_tuples_with_tuples_with_tuples_with_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return tuple([tuple([x[0] - x[1] for x in a]), tuple([x[0] * x[1] for x in a]), sum([x[1] + x[1] for x in a])])


def make_tuple_of_tuples_with_tuples_with_tuples_with_tuples_with_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return tuple([tuple([x[0] - x[1] for x in a]), tuple([x[0] * x[1] for x in a]), sum([x[1] + x[1] for x in a])])


def make_tuple_of_tuples_with_tuples_with_tuples_with_tuples_with_tuples_with_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    return tuple([tuple([x[0] - x[1] for x in 