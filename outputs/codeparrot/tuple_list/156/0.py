def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest second value.
    """
    return max(lst, key=lst[0])[1]


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the largest second value.
    """
    return max(lst, key=lst[1])[0]


def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest second value.
    """
    return max(lst, key=lst[2])[1]


def get_value_from_list_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest second value.
    """
    return max(lst, key=lst[3])[0]


def get_value_from_list_with_max_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the largest second value.
    """
    return max(lst, key=lst[4])[1]


def get_value_from_list_with_min_value_and_max_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest second value and the largest second value.
    """
    return max(lst, key=lst[5])[1]


def get_value_from_list_with_max_value_and_min_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the largest second value and the smallest second value.
    """
    return max(lst, key=lst[6])[1]


def get_value_from_list_with_min_value_and_max_value_and_min_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest second value and the largest second value.
    """
    return max(lst, key=lst[7])[1]


def get_value