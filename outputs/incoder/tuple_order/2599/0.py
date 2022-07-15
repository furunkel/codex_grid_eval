
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    return (b + a, a * b, a - b)


def make_tuple_of_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the sum of the first element of each tuple.
    The third element contains the product of the first element of each tuple.
    The first element contains the difference of the second element of each tuple (first - second).
    """
    return sum(a, ()) + a[0] * a[1]


def make_tuple_of_lists(a):
    """
    Given a list of lists, return a tuple where:
    The second element contains the sum of the first element of each list.
    The third element contains the product of the first element of each list.
    The first element contains the difference of the second element of each list (first - second).
    """
    return sum(a, ()) + a[0] * a[1]


def make_tuple_of_sets(a):
    """
    Given a list of sets, return a tuple where:
    The second element contains the sum of the first element of each set.
    The third element contains the product of the first element of each set.
    The first element contains the difference of the second element of each set (first - second).
    """
    return sum(a, ()) + a[0] * a[1]


def make_tuple_of_dicts(a):
    """
    Given a list of dicts, return a tuple where:
    The second element contains the sum of the first element of each dict.
    The third element contains the product of the first element of each dict.
    The first element contains the difference of the second element of each dict (first - second).
    """
    return sum(a, ()) + a[0] * a[1]


def make_tuple_of_strings(a):
    """
    Given a list of strings, return a tuple where:
    The second element contains the sum of the first element of each string.
    The third element contains the product of the first element of each string.
    The first element contains the difference of the second element of each string (first - second).
    """
    return sum(a, ()) + a[0] * a[1]


def make_tuple_of_ints(a):
    """
    Given a list of ints, return a tuple where:
    The second element contains the sum of the first element of each int.
    The third element contains the product of the first element of each int.
    The first element contains the difference of the second element of each int (first - second).
    """
    return sum(a, ()) + a[0] * a[1]


def make_tuple_of_floats(a):
    """
    Given a list of floats, return a tuple where:
    The second element contains the sum of the first element of each float.
    The third element contains the product of the first element of each float.
    The first element contains the difference of the second element of each float (first - second).
    """
    return sum(a, ()) + a[0] * a[1]


def make_tuple_of_bools(a):
    """
    Given a list of bools, return a tuple where:
