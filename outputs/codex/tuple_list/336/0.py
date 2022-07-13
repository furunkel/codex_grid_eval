
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lambda x: x[10])[10]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the eleventh values of the tuples with the smallest eleventh values.
    """
    return [x[10] for x in lst if x[10] == min(lst, key=lambda x: x[10])[10]]


def extract_values_2(lst):
    """
    Given a list of tuples, write a function that returns a list of the eleventh values of the tuples with the smallest eleventh values.
    """
    return [x[10] for x in lst if x[10] == min(x[10] for x in lst)]


def extract_values_3(lst):
    """
    Given a list of tuples, write a function that returns a list of the eleventh values of the tuples with the smallest eleventh values.
    """
    return [x[10] for x in lst if x[10] == min(x[10] for x in lst)]


def extract_values_4(lst):
    """
    Given a list of tuples, write a function that returns a list of the eleventh values of the tuples with the smallest eleventh values.
    """
    return [x[10] for x in lst if x[10] == min(x[10] for x in lst)]


def extract_values_5(lst):
    """
    Given a list of tuples, write a function that returns a list of the eleventh values of the tuples with the smallest eleventh values.
    """
    return [x[10] for x in lst if x[10] == min(x[10] for x in lst)]


def extract_values_6(lst):
    """
    Given a list of tuples, write a function that returns a list of the eleventh values of the tuples with the smallest eleventh values.
    """
    return [x[10] for x in lst if x[10] == min(x[10] for x in lst)]


def