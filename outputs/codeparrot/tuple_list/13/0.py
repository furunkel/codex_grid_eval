def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return tuple(lst[0])


def tuple_concat(lst):
    """
    Given a list of tuples, write a function that returns the concatenation of the two values.
    """
    return tuple(lst[0]) + tuple(lst[1])


def tuple_split(lst):
    """
    Given a list of tuples, write a function that returns the two values.
    """
    return tuple(lst[0]), tuple(lst[1])


def tuple_join(lst):
    """
    Given a list of tuples, write a function that returns the concatenation of the two values.
    """
    return tuple(lst[0]), tuple(lst[1])


def tuple_split_by_index(lst, index):
    """
    Given a list of tuples, write a function that returns the two values.
    """
    return tuple(lst[0]), tuple(lst[1])[:index]


def tuple_split_by_value(lst, value):
    """
    Given a list of tuples, write a function that returns the two values.
    """
    return tuple(lst[0]), tuple(lst[1])[:value]


def tuple_split_by_index_value(lst, index, value):
    """
    Given a list of tuples, write a function that returns the two values.
    """
    return tuple(lst[0]), tuple(lst[1])[:index] + tuple(lst[2:])[:value]


def tuple_split_by_value_and_index(lst, value, index):
    """
    Given a list of tuples, write a function that returns the two values.
    """
    return tuple(lst[0]), tuple(lst[1])[:index] + tuple(lst[2:])[:index] + tuple(lst[3:])[:value]


def tuple_split_by_value_and_index_value(lst, value, index, value):
    """
    Given a list of tuples, write a function that returns the two values.
    """
    return tuple(lst[0]), tuple(lst[1])[:index] + tuple(lst[2:])[:index] + tuple(lst[3:])[:value]


def