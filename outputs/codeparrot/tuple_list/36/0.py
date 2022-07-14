def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lambda x: x[1])[0]


def get_twelfth_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[0]


def get_twelfth_value_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lambda x: x[1])[0]


def get_twelfth_value_with_max_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[0]


def get_twelfth_value_with_min_value_and_max_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value and the largest twelfth value.
    """
    return min(lst, key=lambda x: x[1])[0], max(lst, key=lambda x: x[1])[0]


def get_twelfth_value_with_min_value_and_max_value_and_min_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value and the largest twelfth value and the smallest twelfth value.
    """
    return min(lst, key=lambda x: x[1])[0], min(lst, key=lambda x: x[1])[0], max(lst, key=lambda x: x[1])[0], min(lst, key=lambda x: x[1])[0]


def get_twelfth_value_with_max_value_and_min