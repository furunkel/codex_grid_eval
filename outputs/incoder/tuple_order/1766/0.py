
def make_tuple(a, fekjfwoeifjwu5gfd):
    """
    Given two integers a and fekjfwoeifjwu5gfd, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    summe = a + fekjfwoeifjwu5gfd
    differenz = a - fekjfwoeifjwu5gfd
    product = a * fekjfwoeifjwu5gfd
    return differenz, summe, product


def make_tuple_of_tuples(a):
    """
    Given a list of integers, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    differenz = []
    summe = []
    product = []
    for x in a:
        differenz, summe, product = make_tuple(x, differenz, summe, product)
    return differenz, summe, product


def make_tuple_of_tuples_2(a):
    """
    Given a list of integers, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    differenz = []
    summe = []
    product = []
    for x in a:
        differenz, summe, product = make_tuple_2(x, differenz, summe, product)
    return differenz, summe, product


def make_tuple_of_tuples_3(a):
    """
    Given a list of integers, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    differenz = []
    summe = []
    product = []
    for x in a:
        differenz, summe, product = make_tuple_3(x, differenz, summe, product)
    return differenz, summe, product


def make_tuple_of_tuples_4(a):
    """
    Given a list of integers, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    differenz = []
    summe = []
    product = []
    for x in a:
        differenz, summe, product = make_tuple_4(x, differenz, summe, product)
    return differenz, summe, product


def make_tuple_of_tuples_5(a):
    """
    Given a list of integers, return a tuple where:
    The second element contains the difference of the two numbers (first - second).
    The first element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    """
    differenz = []