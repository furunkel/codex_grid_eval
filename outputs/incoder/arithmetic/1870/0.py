
def make_tuple(a, fekjfwoeifjwu5gfd):
    """
    Given two integers a and fekjfwoeifjwu5gfd, return a tuple where:
    The second element contains the sum of the two numbers.
    The third element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    summe = a + fekjfwoeifjwu5gfd
    product = a * fekjfwoeifjwu5gfd
    difference = a - fekjfwoeifjwu5gfd
    return summe, product, difference


def make_tuple_of_tuples(a):
    """
    Given a list of integers, return a tuple of tuples where:
    The second element of each tuple contains the sum of the two numbers.
    The third element of each tuple contains the product of the two numbers.
    The first element of each tuple contains the difference of the two numbers.
    """
    tuples = []
    for element in a:
        summe, product, difference = make_tuple(element, element)
        tuples.append((summe, product, difference))
    return tuples


def make_tuple_of_tuples_of_tuples(a):
    """
    Given a list of lists of integers, return a tuple of tuples where:
    The second element of each tuple contains the sum of the two numbers.
    The third element of each tuple contains the product of the two numbers.
    The first element of each tuple contains the difference of the two numbers.
    """
    tuples = []
    for element in a:
        tuples_of_tuples = []
        for sublist in element:
            summe, product, difference = make_tuple(sublist, sublist)
            tuples_of_tuples.append((summe, product, difference))
        tuples.append(tuples_of_tuples)
    return tuples


def make_tuple_of_tuples_of_tuples(a):
    """
    Given a list of lists of lists of integers, return a tuple of tuples where:
    The second element of each tuple contains the sum of the two numbers.
    The third element of each tuple contains the product of the two numbers.
    The first element of each tuple contains the difference of the two numbers.
    """
    tuples = []
    for element in a:
        tuples_of_tuples_of_tuples = []
        for sublist in element:
            tuples_of_tuples_of_tuples = []
            for sublist_2 in sublist:
                summe, product, difference = make_tuple(sublist_2, sublist_2)
                tuples_of_tuples_of_tuples.append((summe, product, difference))
            tuples_of_tuples_of_tuples.append(tuples_of_tuples_of_tuples)
        tuples.append(tuples_of_tuples_of_tuples)
    return tuples


def make_tuple_of_tuples_of_tuples_of_tuples(a):
    """
    Given a list of lists of lists of lists of integers, return a tuple of tuples where:
    The second element of each tuple contains the sum of the two numbers.
    The third element of each tuple contains the product of the two numbers.
    The first element of each tuple contains the difference of the two numbers.
    """
    tuples = []
    for element in a:
        tuples_of_tuples_of_tuples_of_tuples = []
        for sublist in element: