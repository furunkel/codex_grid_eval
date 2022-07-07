
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[1]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple.
    """
    return [x[1] for x in text]


def extract_keys(text):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple.
    """
    return [x[0] for x in text]


def extract_key_value(text):
    """
    Given a list of tuples, write a function that returns a dictionary of the first values of each tuple as keys and the
    second values of each tuple as values.
    """
    return {x[0]: x[1] for x in text}


def extract_key_value_reverse(text):
    """
    Given a list of tuples, write a function that returns a dictionary of the second values of each tuple as keys and the
    first values of each tuple as values.
    """
    return {x[1]: x[0] for x in text}


def extract_key_value_reverse_duplicate(text):
    """
    Given a list of tuples, write a function that returns a dictionary of the second values of each tuple as keys and the
    first values of each tuple as values. If there are duplicate second values, the function should return the first
    value of the tuple with the duplicate second value.
    """
    return {x[1]: x[0] for x in text}


def extract_key_value_reverse_duplicate_list(text):
    """
    Given a list of tuples, write a function that returns a dictionary of the second values of each tuple as keys and the
    first values of each tuple as values. If there are duplicate second values, the function should return a list of the
    first values of the tuples with the duplicate second values.
    """
    return {x[1]: [y[0] for y in text if y[1] == x[1]] for x in text}


def extract_key_value_reverse_duplicate_list_sorted(