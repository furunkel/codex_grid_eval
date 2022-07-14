def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest eleventh value.
    """
    return max(lst, key=lambda x: x[1])[0]


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lambda x: x[1])[1]


def get_value_at_index(lst, index):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest eleventh value.
    """
    return min(lst, key=lambda x: x[1])[index]


def get_value_at_index_and_value(lst, index, value):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest eleventh value and the value.
    """
    return min(lst, key=lambda x: x[1])[index][value]


def get_value_at_index_and_value_at_index(lst, index, value, value_at_index):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest eleventh value and the value.
    """
    return min(lst, key=lambda x: x[1])[index][value_at_index]


def get_value_at_index_and_value_at_index_and_value(lst, index, value, value_at_index_and_value):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest eleventh value and the value.
    """
    return min(lst, key=lambda x: x[1])[index][value_at_index_and_value]


def get_value_at_index_and_value_at_index_and_value_at_index(lst, index, value, value_at_index_and_value_at_index):
    """
    Given a list of tuples, write a function that returns the t