
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest last value.
    """
    return min(lst, key=lambda x: x[1])[0]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with the smallest last value.
    """
    return [x[0] for x in lst if x[1] == min(lst, key=lambda x: x[1])[1]]


def extract_values_set(lst):
    """
    Given a list of tuples, write a function that returns a set of the first values of each tuple with the smallest last value.
    """
    return {x[0] for x in lst if x[1] == min(lst, key=lambda x: x[1])[1]}


def extract_values_dict(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the first values of each tuple with the smallest last value.
    """
    return {x[0]: x[1] for x in lst if x[1] == min(lst, key=lambda x: x[1])[1]}


def extract_values_dict_2(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the first values of each tuple with the smallest last value.
    """
    return {x[0]: x[1] for x in lst if x[1] == min(lst, key=lambda x: x[1])[1]}


def extract_values_dict_3(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the first values of each tuple with the smallest last value.
    """
    return {x[0]: x[1] for x in lst if x[1] == min(lst, key=lambda x: x[1])[1]}


def extract_values_dict_4(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the first values of each tuple with the smallest last value.
    """
    return {x[0]: x[1] for x