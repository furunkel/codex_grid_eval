def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest last value.
    """
    return max(lst, key=lst.count)[0]


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lst.count)[1]


def get_first_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst, key=lst.count)[0]


def get_last_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
    return max(lst, key=lst.count)[1]


def get_first_value_with_last_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value and the last value.
    """
    return max(lst, key=lst.count)[0]


def get_last_value_with_first_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value and the last value.
    """
    return max(lst, key=lst.count)[1]


def get_first_value_with_last_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value and the last value.
    """
    return min(lst, key=lst.count)[0]


def get_last_value_with_first_value_with_last_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value and the last value.
    """
    return max(lst, key=lst.count)[1]


def get_first_value_with_last_value_with_first_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value