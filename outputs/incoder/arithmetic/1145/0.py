
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    return (a-b, a+b, a*b)

def make_tuple_of_tuples(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    tuple_of_tuples = []
    for tuple_of_tuples in list_of_tuples:
        tuple_of_tuples.append(make_tuple(tuple_of_tuples[0], tuple_of_tuples[1]))
    return tuple_of_tuples

def make_tuple_of_tuples_2(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    tuple_of_tuples = []
    for tuple_of_tuples in list_of_tuples:
        tuple_of_tuples.append(make_tuple_of_tuples(tuple_of_tuples))
    return tuple_of_tuples

def make_tuple_of_tuples_3(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    tuple_of_tuples = []
    for tuple_of_tuples in list_of_tuples:
        tuple_of_tuples.append(make_tuple_of_tuples_2(tuple_of_tuples))
    return tuple_of_tuples

def make_tuple_of_tuples_4(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    tuple_of_tuples = []
    for tuple_of_tuples in list_of_tuples:
        tuple_of_tuples.append(make_tuple_of_tuples_3(tuple_of_tuples))
    return tuple_of_tuples

def make_tuple_of_tuples_5(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The third element contains the sum of the two numbers.
    The first element contains the product of the two numbers.
    """
    tuple_of_tuples = []
    for tuple_of_tuples in list_of_tuples:
        tuple_of_tuples.append(make_tuple_of_tuples_4(tuple_of_tuples))
    return tuple_of_tuples

def make_tuple_of_tuples_6(list_of_tuples):
    """
    Given a list of tuples, return a tuple where:
    The second element contains the difference of the two numbers (first 