def incr_list(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list([1, 2, 3])
    [3, 4, 5]
    """
    return [x + y for x, y in zip(l[::2], l[1::2])]


def incr_list_with_index(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list_with_index([1, 2, 3])
    [3, 4, 5]
    """
    return [x + y for x, y in zip(l[::2], l[1::2], l[2::2])]


def incr_list_with_slice(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list_with_slice([1, 2, 3])
    [3, 4, 5]
    """
    return [x + y for x, y in zip(l[::2], l[1::2], l[2::2])]


def incr_list_with_slice_index(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list_with_slice_index([1, 2, 3])
    [3, 4, 5]
    """
    return [x + y for x, y in zip(l[::2], l[1::2], l[2::2])]


def incr_list_with_slice_slice(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list_with_slice_slice([1, 2, 3])
    [3, 4, 5]
    """
    return [x + y for x, y in zip(l[::2], l[1::2], l[2::2], l[3::2])]


def incr_list_with_slice_slice_index(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list_with_slice_slice_index([1, 2, 3])
    [3, 4, 5]
    """
    return [x + y for x, y in zip(l[::2], l[1::2], l[2::2], l[3::2])]


