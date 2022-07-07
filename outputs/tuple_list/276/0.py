
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return min(text, key=lambda x: x[-1])[11]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return [x[11] for x in text]


def extract_values_2(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return [x[11] for x in text if x[11] != 'NA']


def extract_values_3(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return [x[11] for x in text if x[11] != 'NA' and x[11] != '0']


def extract_values_4(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return [x[11] for x in text if x[11] != 'NA' and x[11] != '0' and x[11] != '0.0']


def extract_values_5(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return [x[11] for x in text if x[11] != 'NA' and x[11] != '0' and x[11] != '0.0' and x[11] != '0.00']


def extract_values_6(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return [x[11] for x in text if x[11] != 'NA' and x[11] != '0' and x[11] != '0.0' and x[11] != '0.00' and x[11] != '0.000']


def extract_values_7(text