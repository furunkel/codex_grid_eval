def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest first value.
    """
    return max(lst, key=lst.count)[0]


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[1]


def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[2]


def get_value_from_list_with_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[3]


def get_value_from_list_with_min(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest second value.
    """
    return min(lst, key=lst.count)[0]


def get_value_from_list_with_mean(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest second value.
    """
    return mean(lst, key=lst.count)[0]


def get_value_from_list_with_median(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest second value.
    """
    return median(lst, key=lst.count)[0]


def get_value_from_list_with_std(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest second value.
    """
    return std(lst, key=lst.count)[0]


def get_value_from_list_with_var(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest second value.
    """
    return var(lst, key=lst.count)[0]


def