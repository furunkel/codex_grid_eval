def incr_list(l: list):
    """Return list with elements incremented by 9999.
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [10004, 10002, 10004, 10001, 10002, 10002, 10008, 9999, 10122]
    """
    return [x for x in l if x > 9999]


def incr_list_with_index(l: list):
    """Return list with elements incremented by 9999.
    >>> incr_list_with_index([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [10004, 10002, 10004, 10001, 10002, 10008, 9999, 10122]
    """
    return [x for x in l if x > 9999]


def incr_list_with_index_with_value(l: list):
    """Return list with elements incremented by 9999.
    >>> incr_list_with_index_with_value([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [10004, 10002, 10004, 10001, 10002, 10008, 9999, 10122]
    """
    return [x for x in l if x > 9999]


def incr_list_with_index_with_value_and_index(l: list):
    """Return list with elements incremented by 9999.
    >>> incr_list_with_index_with_value_and_index([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [10004, 10002, 10004, 10001, 10002, 10008, 9999, 10122]
    """
    return [x for x in l if x > 9999 and x < 9999]


def incr_list_with_index_with_value_and_index_with_index(l: list):
    """Return list with elements incremented by 9999.
    >>> incr_list_with_index_with_value_and_index([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [10004, 10002, 10004, 10001, 10002,