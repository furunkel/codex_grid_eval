def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    return max(lst, key=lst.count)


def get_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest value.
    """
    return max(lst, key=lst.count)[-1]


def get_value_at_index(lst, index):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest value.
    """
    return max(lst, key=lst.index)[-1]


def get_value_at_index_and_value(lst, index, value):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest value and the value.
    """
    return max(lst, key=lst.index)[-1]


def get_value_at_index_and_value_and_index(lst, index, value, index_and_value):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest value and the value and the index.
    """
    return max(lst, key=lst.index)[-1]


def get_value_at_index_and_value_and_index_and_value(lst, index, value, index_and_value, value_and_index):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest value and the value and the index.
    """
    return max(lst, key=lst.index)[-1]


def get_value_at_index_and_value_and_index_and_value_and_index(lst, index, value, index_and_value, value_and_index_and_value):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest value and the value and the index and the value and the index and the value and the index and the value and the value and the index and the value and the value and