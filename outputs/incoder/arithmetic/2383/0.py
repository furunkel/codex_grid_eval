
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    """
    return (b + a, a * b, a - b)


def make_tuple_of_tuples(tuple_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The third element contains the product of the second element of each tuple.
    The second element contains the difference of the second element of each tuple (first - second).
    """
    sum_tuple = tuple_of_tuples[0]
    product_tuple = tuple_of_tuples[1]
    diff_tuple = tuple_of_tuples[2]
    for t in tuple_of_tuples:
        sum_tuple += t[0]
        product_tuple *= t[1]
        diff_tuple -= t[2]
    return sum_tuple, product_tuple, diff_tuple


def make_tuple_of_tuples_2(tuple_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The third element contains the product of the second element of each tuple.
    The second element contains the difference of the second element of each tuple (first - second).
    """
    sum_tuple = tuple_of_tuples[0]
    product_tuple = tuple_of_tuples[1]
    diff_tuple = tuple_of_tuples[2]
    for t in tuple_of_tuples:
        sum_tuple += t[0]
        product_tuple *= t[1]
        diff_tuple -= t[2]
    return sum_tuple, product_tuple, diff_tuple


def make_tuple_of_tuples_3(tuple_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The third element contains the product of the second element of each tuple.
    The second element contains the difference of the second element of each tuple (first - second).
    """
    sum_tuple = tuple_of_tuples[0]
    product_tuple = tuple_of_tuples[1]
    diff_tuple = tuple_of_tuples[2]
    for t in tuple_of_tuples:
        sum_tuple += t[0]
        product_tuple *= t[1]
        diff_tuple -= t[2]
    return sum_tuple, product_tuple, diff_tuple


def make_tuple_of_tuples_4(tuple_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The third element contains the product of the second element of each tuple.
    The second element contains the difference of the second element of each tuple (first - second).
    """
    sum_tuple = tuple_of_tuples[0]
    product_tuple = tuple_of_tuples[1]
    diff_tuple = tuple_of_tuples[2]
    for t in tuple_of_tuples:
        sum_tuple += t[0]
        product_tuple *= t[1]
