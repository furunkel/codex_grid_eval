
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return max(text, key=lambda x: x[-1])[11]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return [x[11] for x in text]


def extract_values_2(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return [x[11] for x in text if x[-1] == max(text, key=lambda x: x[-1])[-1]]


def extract_values_3(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return [x[11] for x in text if x[-1] == max(text, key=lambda x: x[-1])[-1] and x[0] == min(text, key=lambda x: x[0])[0]]


def extract_values_4(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return [x[11] for x in text if x[-1] == max(text, key=lambda x: x[-1])[-1] and x[0] == min(text, key=lambda x: x[0])[0] and x[1] == min(text, key=lambda x: x[1])[1]]


def extract_values_5(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return [x[11] for x in text if x[-1] == max(text, key=lambda x: x[-1])[-1] and x[0] == min(text, key=lambda x: x[0])[0] and x[1] == min(text, key=lambda x: x[1])[1] and x[