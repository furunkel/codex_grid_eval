def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[0]


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[1]


def get_value_from_list(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[2]


def get_value_from_list_with_smallest_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[3]


def get_value_from_list_with_largest_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[4]


def get_value_from_list_with_smallest_value_and_largest_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest eleventh value and the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[5]


def get_value_from_list_with_smallest_value_and_smallest_value(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the smallest eleventh value and the largest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[6]


def get_value_from_list_with_largest_value_and_largest_value(lst):
    """
    Given a list of tuples, write a function that