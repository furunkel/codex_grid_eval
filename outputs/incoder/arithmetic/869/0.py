
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The first element contains the sum of the two numbers.
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    """
    return (a+b, a-b, a*b)


def make_tuple_of_tuples(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the difference of the second element of each tuple.
    The third element contains the product of the third element of each tuple.
    """
    sum_tuple = ()
    diff_tuple = ()
    prod_tuple = ()
    for tup in list_of_tuples:
        sum_tuple += tup
        diff_tuple += tup
        prod_tuple += tup
    return sum_tuple, diff_tuple, prod_tuple


def make_tuple_of_lists(list_of_lists):
    """
    Given a list of lists, return a tuple where:
    The first element contains the sum of the first element of each list.
    The second element contains the difference of the second element of each list.
    The third element contains the product of the third element of each list.
    """
    sum_tuple = ()
    diff_tuple = ()
    prod_tuple = ()
    for lis in list_of_lists:
        sum_tuple += lis
        diff_tuple += lis
        prod_tuple += lis
    return sum_tuple, diff_tuple, prod_tuple


def make_tuple_of_sets(list_of_sets):
    """
    Given a list of sets, return a tuple where:
    The first element contains the sum of the first element of each set.
    The second element contains the difference of the second element of each set.
    The third element contains the product of the third element of each set.
    """
    sum_tuple = ()
    diff_tuple = ()
    prod_tuple = ()
    for lis in list_of_sets:
        sum_tuple += lis
        diff_tuple += lis
        prod_tuple += lis
    return sum_tuple, diff_tuple, prod_tuple


def make_tuple_of_dicts(list_of_dicts):
    """
    Given a list of dicts, return a tuple where:
    The first element contains the sum of the first element of each dict.
    The second element contains the difference of the second element of each dict.
    The third element contains the product of the third element of each dict.
    """
    sum_tuple = ()
    diff_tuple = ()
    prod_tuple = ()
    for lis in list_of_dicts:
        sum_tuple += lis
        diff_tuple += lis
        prod_tuple += lis
    return sum_tuple, diff_tuple, prod_tuple


def make_tuple_of_mixed_tuples_and_lists(list_of_tuples_and_lists):
    """
    Given a list of tuples and lists, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the difference of the 