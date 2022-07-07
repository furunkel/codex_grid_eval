
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(text, key=lambda x: x[0])[0]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest
    first values.
    """
    return [x[1] for x in text if x[0] == extract_value(text)]


def extract_values_2(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest
    first values.
    """
    return [x[1] for x in text if x[0] == min(text, key=lambda x: x[0])[0]]


def extract_values_3(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest
    first values.
    """
    return [x[1] for x in text if x[0] == min(text)[0]]


def extract_values_4(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest
    first values.
    """
    return [x[1] for x in text if x[0] == min(x[0] for x in text)]


def extract_values_5(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest
    first values.
    """
    return [x[1] for x in text if x[0] == min(x[0] for x in text)]


def extract_values_6(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples with the smallest
    first values.
    """
    return [x[1] for x in text if x[0] == min(x[0] for x in text)]


def extract_values_7(text):
    """
    Given a list of tuples, write a function that returns a list of the