def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return max(lst, key=lst[0])[1]


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lst[0])[1]


def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return max(lst, key=lst[0])[1]


def get_value_from_list_with_min(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lst[0])[1]


def get_value_from_list_with_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
    return max(lst, key=lst[0])[1]


def get_value_from_list_with_min_and_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lst[0])[1], max(lst, key=lst[0])[1]


def get_value_from_list_with_max_and_min(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
    return max(lst, key=lst[0])[1], min(lst, key=lst[0])[1]


def get_value_from_list_with_min_and_max_and_min(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lst[0])[1], max(lst, key=lst[0])[1], min(lst, key=lst[0])[