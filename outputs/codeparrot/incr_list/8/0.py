def incr_list(l: list):
    """Return list with elements incremented by 9999.
    >>> incr_list([1, 2, 3])
    [10000, 10001, 10002]
    """
    return [x for x in l if x > 9999]


def incr_list_with_index(l: list):
    """Return list with elements incremented by 9999.
    >>> incr_list_with_index([1, 2, 3], 0)
    [10000, 10001, 10002]
    """
    return [x for x in l if x > 9999]


def incr_list_with_index_with_value(l: list, value: int):
    """Return list with elements incremented by 9999.
    >>> incr_list_with_index_with_value([1, 2, 3], 1)
    [10000, 10001, 10002]
    """
    return [x for x in l if x > 9999 and x < value]


def incr_list_with_index_with_value_with_index(l: list, value: int, index: int):
    """Return list with elements incremented by 9999.
    >>> incr_list_with_index_with_value_with_index([1, 2, 3], 1, index=2)
    [10000, 10001, 10002]
    """
    return [x for x in l if x > 9999 and x < index and x < value]


def incr_list_with_index_with_value_with_index_with_value(l: list, value: int, index: int, value_index: int):
    """Return list with elements incremented by 9999.
    >>> incr_list_with_index_with_value([1, 2, 3], 1, index=2, value_index=3)
    [10000, 10001, 10002]
    """
    return [x for x in l if x > 9999 and x < value and x < index and x < value_index]


def incr_list_with_index_with_value_with_index_with_value_with_index(l: list, value: int, index: int, value_index: int):
    """Return list with elements incre