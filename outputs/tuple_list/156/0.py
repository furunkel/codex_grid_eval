
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[2]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return [x[2] for x in text if x[1] > 5]


def extract_values_2(text):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return list(map(lambda x: x[2], filter(lambda x: x[1] > 5, text)))


def extract_values_3(text):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return [x[2] for x in filter(lambda x: x[1] > 5, text)]


def extract_values_4(text):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return list(map(lambda x: x[2], text))


def extract_values_5(text):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return [x[2] for x in text]


def extract_values_6(text):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return list(map(lambda x: x[2], filter(lambda x: x[1] > 5, text)))


def extract_values_7(text):
    """
    Given a list of tuples, write a function that returns a list of the third values of the tuples with the second value greater than 5.
    """
    return [x[2] for x in filter(lambda x: x[1] > 5