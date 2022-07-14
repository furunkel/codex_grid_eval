def incr_list(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [7, 5, 7, 4, 5, 5, 11, 2, 125]
    """
    return [x + y for x, y in zip(l[::2], l[1::2])]


def incr_list_with_index(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list_with_index([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [7, 5, 7, 4, 5, 5, 11, 2, 125]
    """
    return [x + y for x, y in zip(l[::2], l[1::2], l[2::2])]


def incr_list_with_index_and_value(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list_with_index_and_value([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [7, 5, 7, 4, 5, 5, 11, 2, 125]
    """
    return [x + y for x, y in zip(l[::2], l[1::2], l[2::2], l[3::2])]


def incr_list_with_index_and_value_and_index(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list_with_index_and_value_and_index([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [7, 5, 7, 4, 5, 5, 11, 2, 125]
    """
    return [x + y for x, y in zip(l[::2], l[1::2], l[2::2], l[3::2])]


def incr_list_with_index_and_value_and_index_and_value(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list_with_index_and_value_and_index_and_value([5,