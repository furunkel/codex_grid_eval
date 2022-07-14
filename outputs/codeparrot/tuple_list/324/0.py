def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[0]


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[1]


def get_value_at_index(lst, index):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[index]


def get_value_at_index_and_value(lst, index, value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value.
    """
    return max(lst, key=lambda x: x[1])[index][1]


def get_value_at_index_and_value_and_index(lst, index, value, index_and_value):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value and the index and value.
    """
    return max(lst, key=lambda x: x[1])[index][1][index_and_value]


def get_value_at_index_and_value_and_index_and_value(lst, index, value, index_and_value, value_and_index):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value and the index and value.
    """
    return max(lst, key=lambda x: x[1])[index][1][index_and_value][value_and_index]


def get_value_at_index_and_value_and_index_and_value_and_index(lst, index, value, index_and_value, value_and_index_and_value):
    """
    Given a