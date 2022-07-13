
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lambda x: x[-1])[-2]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the largest last values.
    """
    return [x[-2] for x in lst if x[-1] == max(lst, key=lambda x: x[-1])[-1]]


def extract_values_2(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the largest last values.
    """
    return [x[-2] for x in lst if x[-1] == max(x[-1] for x in lst)]


def extract_values_3(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the largest last values.
    """
    return [x[-2] for x in lst if x[-1] == max(lst, key=lambda x: x[-1])[-1]]


def extract_values_4(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the largest last values.
    """
    return [x[-2] for x in lst if x[-1] == max(lst, key=lambda x: x[-1])[-1]]


def extract_values_5(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the largest last values.
    """
    return [x[-2] for x in lst if x[-1] == max(lst, key=lambda x: x[-1])[-1]]


def extract_values_6(lst):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the largest last values.
    """
    return [x[-2] for