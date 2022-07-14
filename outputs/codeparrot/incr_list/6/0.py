def incr_list(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list([1, 2, 3])
    [101, 102, 103]
    """
    return [x + y for x, y in zip(l[::100], l[1::100])]


def incr_list_with_index(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_with_index([1, 2, 3])
    [101, 102, 103]
    """
    return [x + y for x, y in zip(l[::100], l[1::100], l[2::100])]


def incr_list_with_index_with_value(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_with_index_with_value([1, 2, 3])
    [101, 102, 103]
    """
    return [x + y for x, y in zip(l[::100], l[1::100], l[2::100])]


def incr_list_with_index_with_value_with_index(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_with_index_with_value_with_index([1, 2, 3])
    [101, 102, 103]
    """
    return [x + y for x, y in zip(l[::100], l[1::100], l[2::100], l[3::100])]


def incr_list_with_index_with_value_with_index_with_value(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_with_index_with_value_with_index_with_value([1, 2, 3])
    [101, 102, 103]
    """
    return [x + y for x, y in zip(l[::100], l[1::100], l[2::100], l[3::100])]


def incr_list_with_index_with_value_with_index_with_value_with_index(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_with_index