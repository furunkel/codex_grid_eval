
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[2]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return [x[2] for x in lst if x[1] > 5]


def extract_values_2(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return list(map(lambda x: x[2], filter(lambda x: x[1] > 5, lst)))


def extract_values_3(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return [x[2] for x in filter(lambda x: x[1] > 5, lst)]


def extract_values_4(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return list(map(lambda x: x[2], lst))


def extract_values_5(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return [x[2] for x in lst]


def extract_values_6(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return list(map(lambda x: x[2], filter(lambda x: x[1] > 5, lst)))


def extract_values_7(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return [x[2]