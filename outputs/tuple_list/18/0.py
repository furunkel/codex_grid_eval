
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[0]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a second value greater than 5.
    """
    return [x[0] for x in text if x[1] > 5]


def extract_values_2(text):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a second value greater than 5.
    """
    return list(map(lambda x: x[0], filter(lambda x: x[1] > 5, text)))


def extract_values_3(text):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a second value greater than 5.
    """
    return [x[0] for x in filter(lambda x: x[1] > 5, text)]


def extract_values_4(text):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a second value greater than 5.
    """
    return list(map(lambda x: x[0], text))


def extract_values_5(text):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a second value greater than 5.
    """
    return [x[0] for x in text]


def extract_values_6(text):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a second value greater than 5.
    """
    return list(map(lambda x: x[0], text))


def extract_values_7(text):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple with a second value greater than 5.
    """
    return [x[0] for x in text if x[1] > 5]


def extract_values_8(text):
    """
    Given a list of tu