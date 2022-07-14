def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest third value.
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


def get_value_from_list_with_max_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the largest fourth value.
    """
    return max(lst, key=lst.count)[4]


def get_value_from_list_with_min_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest fourth value.
    """
    return min(lst, key=lst.count)[5]


def get_value_from_list_with_min_value_and_max_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest fourth value and the largest fourth value.
    """
    return min(lst, key=lst.count)[6]


def get_value_from_list_with_max_value_and_min_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the largest fourth value and the smallest fourth value.
    """
    return max(lst, key=lst.count)[7]


def get_value_from_list_with_min_value_and_max_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest fourth value and the largest fourth value.
    """
    return min(lst, key=lst.count)[8]


