
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    return (a-b, b*a, a*b)

def make_tuple_of_tuples(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    return tuple(map(make_tuple, list_of_tuples))

def make_tuple_of_tuples_with_tuple_of_tuples(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    return tuple(map(make_tuple_of_tuples, list_of_tuples))

def make_tuple_of_tuples_with_list_of_tuples(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    return tuple(map(make_tuple_of_tuples, list_of_tuples))

def make_tuple_of_tuples_with_list_of_tuples_with_tuple_of_tuples(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    return tuple(map(make_tuple_of_tuples, list_of_tuples))

def make_tuple_of_tuples_with_list_of_tuples_with_list_of_tuples(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    return tuple(map(make_tuple_of_tuples, list_of_tuples))

def make_tuple_of_tuples_with_list_of_tuples_with_list_of_tuples_with_tuple_of_tuples(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first element contains the sum of the two numbers.
    """
    return tuple(map(make_tuple_of_tuples, list_of_tuples))

def make_tuple_of_tuples_with_list_of_tuples_with_list_of_tuples_with_list_of_tuples(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the product of the two numbers.
    The first 