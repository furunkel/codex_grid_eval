def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[1]


def get_twelfth_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[0]


def get_twelfth_value_with_highest_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the highest value.
    """
    return max(lst, key=lst.count)[-1]


def get_twelfth_value_with_lowest_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the lowest value.
    """
    return min(lst, key=lst.count)[-1]


def get_twelfth_value_with_highest_value_with_lowest_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the highest value.
    """
    return max(lst, key=lst.count)[-1]


def get_twelfth_value_with_lowest_value_with_highest_value_with_lowest_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the lowest value.
    """
    return min(lst, key=lst.count)[-1]


def get_twelfth_value_with_lowest_value_with_highest_value_with_lowest_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the lowest value.
    """
    return max(lst, key=lst.count)[-1]


def get_twelfth_value_with_lowest_value_with_highest_value_with_lowest_value(lst):
    """
    Given a list of tuples, write a