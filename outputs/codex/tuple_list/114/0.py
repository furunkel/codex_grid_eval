
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[11])[1]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with the largest
    twelfth value.
    """
    return [x[1] for x in lst if x[11] == max(lst, key=lambda x: x[11])[11]]


def extract_values_2(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with the largest
    twelfth value.
    """
    return [x[1] for x in lst if x[11] == max(x[11] for x in lst)]


def extract_values_3(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with the largest
    twelfth value.
    """
    return [x[1] for x in lst if x[11] == max(x[11] for x in lst)]


def extract_values_4(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with the largest
    twelfth value.
    """
    return [x[1] for x in lst if x[11] == max(x[11] for x in lst)]


def extract_values_5(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with the largest
    twelfth value.
    """
    return [x[1] for x in lst if x[11] == max(x[11] for x in lst)]


def extract_values_6(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with the largest
    twelfth value.
    """
    return [x[1] for x in lst if x[11] == max(x[11] for x in lst)]


def