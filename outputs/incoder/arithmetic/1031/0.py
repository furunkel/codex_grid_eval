
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The second element contains the sum of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    """
    return (a+b, b-a, a*b)


def make_tuple_of_tuples(a):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the sum of the first element of each tuple.
    The first element contains the difference of the first element of each tuple (first - second).
    The third element contains the product of the first element of each tuple.
    """
    return tuple([sum(t) for t in a]), tuple([sum(t[1:])-sum(t[:-1]) for t in a]), tuple([sum(t[1:])*t[-1] for t in a])


def make_tuple_of_lists(a):
    """
    Given a list of lists, return a tuple where:
    The second element contains the sum of the first element of each list.
    The first element contains the difference of the first element of each list (first - second).
    The third element contains the product of the first element of each list.
    """
    return tuple([sum(t) for t in a]), tuple([sum(t[1:])-sum(t[:-1]) for t in a]), tuple([sum(t[1:])*t[-1] for t in a])


def make_tuple_of_sets(a):
    """
    Given a list of sets, return a tuple where:
    The second element contains the sum of the first element of each set.
    The first element contains the difference of the first element of each set (first - second).
    The third element contains the product of the first element of each set.
    """
    return tuple([sum(t) for t in a]), tuple([sum(t[1:])-sum(t[:-1]) for t in a]), tuple([sum(t[1:])*t[-1] for t in a])


def make_tuple_of_dicts(a):
    """
    Given a list of dicts, return a tuple where:
    The second element contains the sum of the first element of each dict.
    The first element contains the difference of the first element of each dict (first - second).
    The third element contains the product of the first element of each dict.
    """
    return tuple([sum(t) for t in a]), tuple([sum(t[1:])-sum(t[:-1]) for t in a]), tuple([sum(t[1:])*t[-1] for t in a])


def make_tuple_of_mixed_types_list(b):
    """
    Given a list of mixed types, return a tuple where:
    The second element contains the sum of the first element of each mixed type.
    The first element contains the difference of the first element of each mixed type (first - second).
    The third element contains the product of the first element of each mixed type.
    """
    return tuple([sum(t) for t in b]), tuple([sum(t[1:])-sum(t[:-1]) for t in b]), tuple([sum(t[1:])*t[-1] for t in b])


def make_tuple_of_mixed_types_tuple(b):
    """
    Given a list of mixed types, return a tuple where:
    The second element contains the sum of the first element of each mixed type.
    The first element contains the difference of the first element of each mixed type (first - second).
    The third element contains the product of the first element of each mixed type.
    """
    return 