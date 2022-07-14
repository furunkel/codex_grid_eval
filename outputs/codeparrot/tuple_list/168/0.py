def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest third value.
    """
    return max(lst, key=lst.count)[1]


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the largest fourth value.
    """
    return max(lst, key=lst.count)[2]


def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the largest fourth value.
    """
    return max(lst, key=lst.count)[3]


def get_value_from_list_with_max(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the largest fourth value.
    """
    return max(lst, key=lst.count)[4]


def get_value_from_list_with_min(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest fourth value.
    """
    return min(lst, key=lst.count)[5]


def get_value_from_list_with_sum(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the largest fourth value.
    """
    return sum(lst, key=lst.count)[1]


def get_value_from_list_with_min_and_max(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest fourth value.
    """
    return min(lst, key=lst.count)[2]


def get_value_from_list_with_max_and_min(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the largest fourth value.
    """
    return max(lst, key=lst.count)[3]


def get_value_from_list_with_min_and_max_and_sum(lst):
    """
    Given a list of tuples, write a function that returns the