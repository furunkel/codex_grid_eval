
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    """
    sum = a * b
    prod = a * b
    diff = a - b
    return sum, prod, diff


def make_tuple_of_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the product of the first element of each tuple.
    The third element contains the difference of the first element of each tuple (first - second).
    """
    sum = 0
    prod = 1
    diff = 0
    for t in a:
        sum += t[0]
        prod *= t[0]
        diff += t[1]
    return sum, prod, diff


def make_tuple_of_tuples_with_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the product of the first element of each tuple.
    The third element contains the difference of the first element of each tuple (first - second).
    The fourth element contains the sum of the second element of each tuple.
    The fifth element contains the product of the second element of each tuple.
    The sixth element contains the difference of the second element of each tuple (first - second).
    """
    sum = 0
    prod = 1
    diff = 0
    sum_of_tuples = 0
    prod_of_tuples = 1
    diff_of_tuples = 0
    for t in a:
        sum += t[0]
        prod *= t[0]
        diff += t[1]
        sum_of_tuples += t[0]
        prod_of_tuples *= t[0]
        diff_of_tuples += t[1]
    return sum, prod, diff, sum_of_tuples, prod_of_tuples, diff_of_tuples


def make_tuple_of_tuples_with_different_lengths(a):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the product of the first element of each tuple.
    The third element contains the difference of the first element of each tuple (first - second).
    The fourth element contains the sum of the second element of each tuple.
    The fifth element contains the product of the second element of each tuple.
    The sixth element contains the difference of the second element of each tuple (first - second).
    The seventh element contains the sum of the third element of each tuple.
    The eighth element contains the product of the third element of each tuple.
    The ninth element contains the difference of the third element of each tuple (first - second).
    """
    sum = 0
    prod = 1
    diff = 0
    sum_of_tuples = 0
    prod_of_tuples = 1
    diff_of_tuples = 0
    sum_of_tuples_2 = 0
    prod_of_tuples_2