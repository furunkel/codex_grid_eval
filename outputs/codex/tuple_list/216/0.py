
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest first values.
    """
    return [x[1] for x in lst if x[0] == min(lst, key=lambda x: x[0])[0]]


def extract_values_2(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest first values.
    """
    return [x[1] for x in lst if x[0] == min(lst)[0]]


def extract_values_3(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest first values.
    """
    return [x[1] for x in lst if x[0] == min(lst, key=lambda x: x[0])[0]]


def extract_values_4(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest first values.
    """
    return [x[1] for x in lst if x[0] == min(lst, key=lambda x: x[0])[0]]


def extract_values_5(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest first values.
    """
    return [x[1] for x in lst if x[0] == min(lst, key=lambda x: x[0])[0]]


def extract_values_6(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest first values.
    """
    return [x[1] for x in lst if x[0] == min(lst, key=lambda x: x[0])[0]]