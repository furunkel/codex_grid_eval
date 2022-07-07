
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(text, key=lambda x: x[12])[13]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of the last values of each tuple with the largest
    twelfth value.
    """
    max_value = max(text, key=lambda x: x[12])[12]
    return [x[13] for x in text if x[12] == max_value]


def extract_values_v2(text):
    """
    Given a list of tuples, write a function that returns a list of the last values of each tuple with the largest
    twelfth value.
    """
    max_value = max(text, key=lambda x: x[12])[12]
    return [x[13] for x in text if x[12] == max_value]


def extract_values_v3(text):
    """
    Given a list of tuples, write a function that returns a list of the last values of each tuple with the largest
    twelfth value.
    """
    max_value = max(text, key=lambda x: x[12])[12]
    return [x[13] for x in text if x[12] == max_value]


def extract_values_v4(text):
    """
    Given a list of tuples, write a function that returns a list of the last values of each tuple with the largest
    twelfth value.
    """
    max_value = max(text, key=lambda x: x[12])[12]
    return [x[13] for x in text if x[12] == max_value]


def extract_values_v5(text):
    """
    Given a list of tuples, write a function that returns a list of the last values of each tuple with the largest
    twelfth value.
    """
    max_value = max(text, key=lambda x: x[12])[12]
    return [x[13] for x in text if x[12] == max_value]


def extract_values_v6(text):
    """
    Given a list of tuples, write a