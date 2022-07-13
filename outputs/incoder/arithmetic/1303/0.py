
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The third element contains the sum of the two numbers.
    The second element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    sum = a+b
    prod = a*b
    diff = a-b
    return sum, prod, diff


def make_tuple_of_tuples(tuple_of_tuples):
    """
    Given a tuple of tuples, return a tuple where:
    The first element contains the sum of the first element of each tuple.
    The second element contains the product of the first element of each tuple.
    The third element contains the difference of the first element of each tuple (first - second).
    The fourth element contains the sum of the second element of each tuple.
    The fifth element contains the product of the second element of each tuple.
    The sixth element contains the difference of the second element of each tuple (first - second).
    """
    sum_tuple = tuple_of_tuples[0][0]+tuple_of_tuples[1][0]
    prod_tuple = tuple_of_tuples[0][1]*tuple_of_tuples[1][1]
    diff_tuple = tuple_of_tuples[0][2]-tuple_of_tuples[1][2]
    sum_tuple_of_tuples = sum_tuple+tuple_of_tuples[2][0]+tuple_of_tuples[3][0]
    prod_tuple_of_tuples = prod_tuple*tuple_of_tuples[2][1]*tuple_of_tuples[3][1]
    diff_tuple_of_tuples = diff_tuple-tuple_of_tuples[2][2]-tuple_of_tuples[3][2]
    return sum_tuple_of_tuples, prod_tuple_of_tuples, diff_tuple_of_tuples


def make_tuple_of_lists(tuple_of_lists):
    """
    Given a tuple of lists, return a tuple where:
    The first element contains the sum of the first element of each list.
    The second element contains the product of the first element of each list.
    The third element contains the difference of the first element of each list (first - second).
    The fourth element contains the sum of the second element of each list.
    The fifth element contains the product of the second element of each list.
    The sixth element contains the difference of the second element of each list (first - second).
    """
    sum_list = tuple_of_lists[0][0]+tuple_of_lists[1][0]
    prod_list = tuple_of_lists[0][1]*tuple_of_lists[1][1]
    diff_list = tuple_of_lists[0][2]-tuple_of_lists[1][2]
    sum_tuple_of_lists = sum_list+tuple_of_lists[2][0]+tuple_of_lists[3][0]
    prod_tuple_of_lists = prod_list*tuple_of_lists[2][1]*tuple_of_lists[3][1]
    diff_tuple_of_lists = diff_list-tuple_of_lists[2][2]-tuple_of_lists[3][2]
    return sum_tuple_of_lists, prod_tuple_of_lists, diff_tuple_of_lists


def make_tuple_of_sets(tuple_of_sets):
    """
    Given a tuple of sets, return a tuple where:
    The 