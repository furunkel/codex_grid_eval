
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    return min(text, key=lambda x: x[2])[11]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    return [x[11] for x in text]


def extract_values_2(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    return [x[11] for x in text if x[2] == min(text, key=lambda x: x[2])[2]]


def extract_values_3(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    return [x[11] for x in text if x[2] == min(text, key=lambda x: x[2])[2] and x[11] != 'NA']


def extract_values_4(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    return [x[11] for x in text if x[2] == min(text, key=lambda x: x[2])[2] and x[11] != 'NA' and x[11] != '-1']


def extract_values_5(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    return [x[11] for x in text if x[2] == min(text, key=lambda x: x[2])[2] and x[11] != 'NA' and x[11] != '-1' and x[11] != '0']


def extract_values_6(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    return [x[11] for x in text if x[2] == min(text, key=lambda x