def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    return max(lst, key=lst[0])[1]


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    return max(lst, key=lst[-1])[1]


def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    return max(lst, key=lst[0])[0]


def get_value_from_list_with_min_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    return min(lst, key=lst[-1])[0]


def get_value_from_list_with_min_max_and_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value and the smallest last value.
    """
    return max(lst, key=lst[-1])[1], min(lst, key=lst[0])[1]


def get_value_from_list_with_min_max_and_min_and_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value and the smallest last value.
    """
    return min(lst, key=lst[-1])[0], max(lst, key=lst[0])[0], min(lst, key=lst[1])[1], max(lst, key=lst[2])[1]


def get_value_from_list_with_min_max_and_min_and_max_and_min(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value and the smallest last value and the smallest last value.
    """
    return min(lst, key=lst[-1])[0], max(lst, key=lst[0])[0], min(lst, key=lst[1