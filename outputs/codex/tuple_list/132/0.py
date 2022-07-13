
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest last value.
    """
    return min(lst, key=lambda x: x[-1])[1]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple.
    """
    return [x[1] for x in lst]


def extract_values_2(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple.
    """
    return list(map(lambda x: x[1], lst))


def extract_values_3(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple.
    """
    return list(map(itemgetter(1), lst))


def extract_values_4(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple.
    """
    return list(map(operator.itemgetter(1), lst))


def extract_values_5(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple.
    """
    return list(map(lambda x: x[1], lst))


def extract_values_6(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple.
    """
    return [x[1] for x in lst]


def extract_values_7(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple.
    """
    return [x[1] for x in lst]


def extract_values_8(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple.
    """
    return [x[1] for x in lst]


def extract_values_9(lst):
    """
    Given a list of tuples, write a function that returns a list of the