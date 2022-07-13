
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the difference of the two numbers (first - second).
    The first element contains the product of the two numbers.
    """
    return (a+b, a-b, a*b)

def make_tuple_of_tuples(tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the sum of the first element of each tuple.
    The third element contains the difference of the first element of each tuple (first - second).
    The first element contains the product of the second element of each tuple.
    """
    return tuple([sum(t) for t in tuples]), tuple([sum(t[1:])-sum(t[:-1]) for t in tuples]), tuple([t[-1]*t[-2] for t in tuples])

def make_tuple_of_tuples_of_tuples(tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the sum of the first element of each tuple in the list.
    The third element contains the difference of the first element of each tuple in the list (first - second).
    The first element contains the product of the second element of each tuple in the list.
    """
    return tuple([sum(t) for t in tuples]), tuple([sum(t[1:])-sum(t[:-1]) for t in tuples]), tuple([t[-1]*t[-2] for t in tuples])

def make_tuple_of_tuples_of_tuples_of_tuples(tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the sum of the first element of each tuple in the list.
    The third element contains the difference of the first element of each tuple in the list (first - second).
    The first element contains the product of the second element of each tuple in the list.
    """
    return tuple([sum(t) for t in tuples]), tuple([sum(t[1:])-sum(t[:-1]) for t in tuples]), tuple([t[-1]*t[-2] for t in tuples])

def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples(tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the sum of the first element of each tuple in the list.
    The third element contains the difference of the first element of each tuple in the list (first - second).
    The first element contains the product of the second element of each tuple in the list.
    """
    return tuple([sum(t) for t in tuples]), tuple([sum(t[1:])-sum(t[:-1]) for t in tuples]), tuple([t[-1]*t[-2] for t in tuples])

def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_tuples(tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the sum of the first element of each tuple in the list.
    The third element contains the difference of the first element of each tuple in the list (first - second).
    The first element contains the product of the second element of each tuple in the list.
    """
    return tuple([sum(t) for t in tuples]), tuple([sum(t[1:])-sum(t[:-1]) for t in tuples]), tuple([t[-1]*t[-2] for t in tuples])

def make_tuple_of_tuples_of_tuples_of_tuples_of_tuples_of_