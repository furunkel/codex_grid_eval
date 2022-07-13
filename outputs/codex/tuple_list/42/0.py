
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[11])[0]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a twelfth value greater than 5.
    """
    return [x[0] for x in lst if x[11] > 5]


def extract_values_2(lst):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a twelfth value greater than 5.
    """
    return list(map(lambda x: x[0], filter(lambda x: x[11] > 5, lst)))


def extract_values_3(lst):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a twelfth value greater than 5.
    """
    return [x[0] for x in filter(lambda x: x[11] > 5, lst)]


def extract_values_4(lst):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a twelfth value greater than 5.
    """
    return list(map(lambda x: x[0], lst))


def extract_values_5(lst):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a twelfth value greater than 5.
    """
    return [x[0] for x in lst]


def extract_values_6(lst):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a twelfth value greater than 5.
    """
    return list(map(lambda x: x[0], lst))


def extract_values_7(lst):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a twelfth value greater than 5.
    """
    return [x[0] for x in lst if x[11] > 5