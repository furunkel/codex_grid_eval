
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The second element contains the sum of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    """
    return (b + a, b - a, a * b)


def make_tuple_of_tuples(l):
    """
    Given a list of tuples, return a tuple of tuples where:
    The second element of each tuple contains the sum of the two numbers.
    The first element of each tuple contains the difference of the two numbers.
    The third element of each tuple contains the product of the two numbers.
    """
    return tuple([tuple([sum(x) for x in zip(*l)]) for l in zip(*l)])


def make_tuple_of_lists(l):
    """
    Given a list of lists, return a tuple of lists where:
    The second element of each list contains the sum of the two numbers.
    The first element of each list contains the difference of the two numbers.
    The third element of each list contains the product of the two numbers.
    """
    return tuple([[sum(x) for x in zip(*l)] for l in zip(*l)])


def make_tuple_of_sets(l):
    """
    Given a list of sets, return a tuple of sets where:
    The second element of each set contains the sum of the two numbers.
    The first element of each set contains the difference of the two numbers.
    The third element of each set contains the product of the two numbers.
    """
    return tuple([{sum(x) for x in zip(*l)} for l in zip(*l)])


def make_tuple_of_dicts(l):
    """
    Given a list of dictionaries, return a tuple of dictionaries where:
    The second element of each dictionary contains the sum of the two numbers.
    The first element of each dictionary contains the difference of the two numbers.
    The third element of each dictionary contains the product of the two numbers.
    """
    return tuple([{k: sum(x) for x in zip(*v.items())} for v in l])


def make_tuple_of_strings(l):
    """
    Given a list of strings, return a tuple of strings where:
    The second element of each string contains the sum of the two numbers.
    The first element of each string contains the difference of the two numbers.
    The third element of each string contains the product of the two numbers.
    """
    return tuple([sum(x) for x in zip(*l)])


def make_tuple_of_floats(l):
    """
    Given a list of floats, return a tuple of floats where:
    The second element of each float contains the sum of the two numbers.
    The first element of each float contains the difference of the two numbers.
    The third element of each float contains the product of the two numbers.
    """
    return tuple([sum(x) for x in zip(*l)])


def make_tuple_of_ints(l):
    """
    Given a list of integers, return a tuple of integers where:
    The second element of each integer contains the sum of the two numbers.
    The first element of each integer contains the difference of the two numbers.
    The third element of each integer contains the product of the two numbers.
    """
    return tuple([sum(x) for x in zip(*l)])


def make_tuple_of_bools(l):
    """
    Given a list of booleans, return a tuple of booleans 