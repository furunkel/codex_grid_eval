
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    return (b - a), (a * b), (a * b)


def make_tuple_of_tuples(tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    sum = 0
    product = 1
    for t in tuples:
        sum, product, product = make_tuple(sum, product) + t
    return sum, product, product


def make_tuple_of_tuples_2(tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    sum = 0
    product = 1
    for t in tuples:
        sum, product, product = make_tuple_2(sum, product) + t
    return sum, product, product


def make_tuple_of_tuples_3(tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    sum = 0
    product = 1
    for t in tuples:
        sum, product, product = make_tuple_3(sum, product) + t
    return sum, product, product


def make_tuple_of_tuples_4(tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    sum = 0
    product = 1
    for t in tuples:
        sum, product, product = make_tuple_4(sum, product) + t
    return sum, product, product


def make_tuple_of_tuples_5(tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    sum = 0
    product = 1
    for t in tuples:
        sum, product, product = make_tuple_5(sum, product) + t
    return sum, product, product


def make_tuple_of_tuples_6(tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the difference of the two numbers (first - second).
    The 