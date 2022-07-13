
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest
    first values.
    """
    return [x[1] for x in lst if x[0] == min(lst, key=lambda x: x[0])[0]]


def extract_values_set(lst):
    """
    Given a list of tuples, write a function that returns a set of the second values of the tuples with the smallest
    first values.
    """
    return {x[1] for x in lst if x[0] == min(lst, key=lambda x: x[0])[0]}


def extract_values_dict(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the second values of the tuples with the
    smallest first values.
    """
    return {x[1]: x[0] for x in lst if x[0] == min(lst, key=lambda x: x[0])[0]}


def extract_values_dict_2(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the second values of the tuples with the
    smallest first values.
    """
    return {x[1]: x[0] for x in lst if x[0] == min(lst, key=lambda x: x[0])[0]}


def extract_values_dict_3(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the second values of the tuples with the
    smallest first values.
    """
    return {x[1]: x[0] for x in lst if x[0] == min(lst, key=lambda x: x[0])[0]}


def extract_values_dict_4(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the second values of the tuples with the
    smallest first values