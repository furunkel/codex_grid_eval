def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return max(lst, key=lst.count)[0]


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return max(lst, key=lst.count)[0]


def get_value_at_index(lst, index):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return max(lst, key=lst.count)[index]


def get_value_at_index_and_value(lst, index, value):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value and the value.
    """
    return max(lst, key=lst.count)[index][value]


def get_value_at_index_and_value_and_index(lst, index, value, index_value):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value and the value.
    """
    return max(lst, key=lst.count)[index][value][index_value]


def get_value_at_index_and_value_and_index_and_value(lst, index, value, index_value, value_value):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value and the value.
    """
    return max(lst, key=lst.count)[index][value][index_value][value_value]


def get_value_at_index_and_value_and_index_and_value_and_index(lst, index, value, index_value, value_value):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value and the value.
    """
    return max(lst, key=lst.count)[index][value][index_value][value_