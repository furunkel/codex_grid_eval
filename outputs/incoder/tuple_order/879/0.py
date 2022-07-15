
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    diff = a - b
    prod = a * b
    sum = a + b
    return diff, prod, sum


def make_tuple_of_tuples(tuple_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    diffs = []
    prods = []
    sums = []
    for t in tuple_of_tuples:
        diff, prod, sum = make_tuple(*t)
        diffs.append(diff)
        prods.append(prod)
        sums.append(sum)
    return tuple(diffs), tuple(prods), tuple(sums)


def make_tuple_of_tuples_with_tuples(tuple_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    diffs = []
    prods = []
    sums = []
    for t in tuple_of_tuples:
        diff, prod, sum = make_tuple_of_tuples(t)
        diffs.append(diff)
        prods.append(prod)
        sums.append(sum)
    return tuple(diffs), tuple(prods), tuple(sums)


def make_tuple_of_tuples_with_none(tuple_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    diffs = []
    prods = []
    sums = []
    for t in tuple_of_tuples:
        diff, prod, sum = make_tuple_with_none(t)
        diffs.append(diff)
        prods.append(prod)
        sums.append(sum)
    return tuple(diffs), tuple(prods), tuple(sums)


def make_tuple_of_tuples_with_none_and_none(tuple_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    """
    diffs = []
    prods = []
    sums = []
    for t in tuple_of_tuples:
        diff, prod, sum = make_tuple_with_none_and_none(t)
        diffs.append(diff)
        prods.append(prod)
        sums.append(sum)
    return tuple(diffs), tuple(prods), tuple(sums)


def make_tuple_of_tuples_with_none_and_