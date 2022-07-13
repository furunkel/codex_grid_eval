
def make_tuple(b, a):
    """
    Given two integers b and a, return a tuple where:
    The first element contains the sum of the two numbers.
    The second element contains the product of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    """
    return (b + a), (a / b), (b - a)


def make_tuple_of_tuples(*tuples):
    """
    Given any number of tuples, return a tuple where:
    The first element contains the sum of the numbers in the first tuple.
    The second element contains the product of the numbers in the first tuple.
    The third element contains the difference of the numbers in the first tuple (first - second).
    """
    return tuple([sum(t) for t in tuples]),\
           tuple([t[0] * t[1] for t in tuples]),\
           tuple([t[0] - t[1] for t in tuples])


def make_tuple_of_tuples_with_tuples(*tuples):
    """
    Given any number of tuples, return a tuple where:
    The first element contains the sum of the numbers in the first tuple.
    The second element contains the product of the numbers in the first tuple.
    The third element contains the difference of the numbers in the first tuple (first - second).
    """
    return tuple([sum(t) for t in tuples]),\
           tuple([t[0] * t[1] for t in tuples]),\
           tuple([t[0] - t[1] for t in tuples]),\
           tuple([t[0] + t[1] for t in tuples])


def make_tuple_of_tuples_with_different_lengths(*tuples):
    """
    Given any number of tuples, return a tuple where:
    The first element contains the sum of the numbers in the first tuple.
    The second element contains the product of the numbers in the first tuple.
    The third element contains the difference of the numbers in the first tuple (first - second).
    The fourth element contains the difference of the numbers in the first tuple (first - second).
    """
    return tuple([sum(t) for t in tuples]),\
           tuple([t[0] * t[1] for t in tuples]),\
           tuple([t[0] - t[1] for t in tuples]),\
           tuple([t[0] + t[1] for t in tuples]),\
           tuple([t[0] + t[1] - t[2] for t in tuples])


def make_tuple_of_tuples_with_different_lengths_with_tuples(*tuples):
    """
    Given any number of tuples, return a tuple where:
    The first element contains the sum of the numbers in the first tuple.
    The second element contains the product of the numbers in the first tuple.
    The third element contains the difference of the numbers in the first tuple (first - second).
    The fourth element contains the difference of the numbers in the first tuple (first - second).
    The fifth element contains the sum of the numbers in the second tuple.
    The sixth element contains the product of the numbers in the second tuple.
    The seventh element contains the difference of the numbers in the second tuple (first - second).
    The eighth element contains the difference of the numbers in the second tuple (first - second).
    """
    return tuple([sum(t) for t in 