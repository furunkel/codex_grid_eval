
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda x: x[1])[1]


def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple.
    """
    return [x[1] for x in lst]


def extract_keys(lst):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple.
    """
    return [x[0] for x in lst]


def extract_key_value(lst):
    """
    Given a list of tuples, write a function that returns a list of the first values of each tuple.
    """
    return [x for x in lst]


def extract_key_value_dict(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the first values of each tuple as keys and the
    second values of each tuple as values.
    """
    return {x[0]: x[1] for x in lst}


def extract_key_value_dict_2(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the first values of each tuple as keys and the
    second values of each tuple as values.
    """
    return dict(lst)


def extract_key_value_dict_3(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the first values of each tuple as keys and the
    second values of each tuple as values.
    """
    return dict(lst)


def extract_key_value_dict_4(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the first values of each tuple as keys and the
    second values of each tuple as values.
    """
    return dict(lst)


def extract_key_value_dict_5(lst):
    """
    Given a list of tuples, write a function that returns a dictionary of the first values of each tuple as keys and the
    second values of each tuple as values