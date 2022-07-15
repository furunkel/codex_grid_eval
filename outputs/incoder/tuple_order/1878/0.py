
def make_tuple(a, fekjfwoeifjwu5gfd):
    """
    Given two integers a and fekjfwoeifjwu5gfd, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    first, second, third = 0, 0, 0
    first, second = a, fekjfwoeifjwu5gfd
    third = first * second
    return first, second, third


def make_tuple_of_tuples(a):
    """
    Given a list of integers, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    first, second, third = 0, 0, 0
    for x in a:
        first, second, third = make_tuple(first, second), make_tuple(second, third), make_tuple(third, x)
    return first, second, third


def make_tuple_of_tuples_2(a):
    """
    Given a list of integers, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    first, second, third = 0, 0, 0
    for x in a:
        first, second, third = make_tuple_of_tuples(first), make_tuple_of_tuples(second), make_tuple_of_tuples(third, x)
    return first, second, third


def make_tuple_of_tuples_3(a):
    """
    Given a list of integers, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    first, second, third = 0, 0, 0
    for x in a:
        first, second, third = make_tuple_of_tuples_2(first), make_tuple_of_tuples_2(second), make_tuple_of_tuples_2(third, x)
    return first, second, third


def make_tuple_of_tuples_4(a):
    """
    Given a list of integers, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    first, second, third = 0, 0, 0
    for x in a:
        first, second, third = make_tuple_of_tuples_3(first), make_tuple_of_tuples_3(second), make_tuple_of_tuples_3(third, x)
    return first, second, third


def make_tuple_of_tuples_5(a):
    """
    Given a list of integers, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
