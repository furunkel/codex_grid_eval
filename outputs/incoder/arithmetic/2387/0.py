
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The second element contains the product of the two numbers.
    """
    return (b - a), (a * b), (a * b)


def make_tuple_of_tuples(tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers in the first tuple.
    The third element contains the sum of the two numbers in the first tuple.
    The second element contains the product of the two numbers in the first tuple.
    """
    sums = [0] * len(tuples)
    products = [1] * len(tuples)
    for a, b in tuples:
        sums[0] += a - b
        products[0] *= a * b
    return tuple(sums), tuple(products)


def make_tuple_of_tuples_with_tuples(tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers in the first tuple.
    The third element contains the sum of the two numbers in the first tuple.
    The second element contains the product of the two numbers in the first tuple.
    """
    sums = [0] * len(tuples)
    products = [1] * len(tuples)
    for a, b in tuples:
        sums[0] += a - b
        products[0] *= a * b
        sums[1] += b - a
        products[1] *= a * b
    return tuple(sums), tuple(products)


def make_tuple_of_tuples_with_tuples_of_tuples(tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers in the first tuple.
    The third element contains the sum of the two numbers in the first tuple.
    The second element contains the product of the two numbers in the first tuple.
    """
    sums = [0] * len(tuples)
    products = [1] * len(tuples)
    for a, b, c in tuples:
        sums[0] += a - b
        products[0] *= a * b
        sums[1] += b - a
        products[1] *= a * b
        sums[2] += c - b
        products[2] *= a * b
        sums[3] += b - c
        products[3] *= a * b
        sums[4] += c - a
        products[4] *= a * b
    return tuple(sums), tuple(products)


def make_tuple_of_tuples_with_tuples_of_tuples_of_tuples(tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers in the first tuple.
    The third element contains the sum of the two numbers in the first tuple.
    The second element contains the product of the two numbers in the first tuple.
    """
    sums = [0] * len(tuples)
    products = [1] * len(tuples)
    for a, b, c, d in tuples:
        sums[0] += a - b
        products[0] *= a * b
        sums[1] += b - a
