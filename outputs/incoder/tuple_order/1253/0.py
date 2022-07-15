
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The third element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The second element contains the product of the two numbers.
    """
    return (a-b, b+a, a*b)


def make_tuple_of_tuples(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the product of the second element of each tuple.
    The third element contains the difference of the second element of each tuple.
    """
    return make_tuple(sum(list_of_tuples[0]), reduce(lambda x, y: x*y, list_of_tuples[1]), reduce(lambda x, y: x*y, map(lambda x, y: x-y, list_of_tuples[1])))


def make_tuple_of_tuples_2(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the product of the second element of each tuple.
    The third element contains the difference of the second element of each tuple.
    """
    return make_tuple(sum(list_of_tuples[0]), reduce(lambda x, y: x*y, list_of_tuples[1]), reduce(lambda x, y: x*y, map(lambda x, y: x-y, list_of_tuples[1])))


def make_tuple_of_tuples_3(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the product of the second element of each tuple.
    The third element contains the difference of the second element of each tuple.
    """
    return make_tuple(sum(list_of_tuples[0]), reduce(lambda x, y: x*y, list_of_tuples[1]), reduce(lambda x, y: x*y, map(lambda x, y: x-y, list_of_tuples[1])))


def make_tuple_of_tuples_4(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the product of the second element of each tuple.
    The third element contains the difference of the second element of each tuple.
    """
    return make_tuple(sum(list_of_tuples[0]), reduce(lambda x, y: x*y, list_of_tuples[1]), reduce(lambda x, y: x*y, map(lambda x, y: x-y, list_of_tuples[1])))


def make_tuple_of_tuples_5(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the product of the second element of each tuple.
    The third element contains the difference of the second element of each tuple.
    """
    return make_tuple(sum(list_of_tuples[0]), reduce(lambda x, y: x*y, list_of_tuples[1]), reduce(lambda x, y: x*y, map(lambda x, y: x-y, list_of_tuples[1])))


def make_tuple_of_tuples_6(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the 