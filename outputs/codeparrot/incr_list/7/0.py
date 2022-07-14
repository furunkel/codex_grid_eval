def incr_list(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [105, 103, 105, 102, 103, 103, 109, 100, 223]
    """
    return [x + y for x, y in zip(l, l[1:])]


def incr_list_with_length(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_with_length([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [105, 103, 105, 102, 103, 103, 109, 100, 223]
    """
    return [x + y for x, y in zip(l, l[1:])]


def incr_list_with_index(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_with_index([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [105, 103, 105, 102, 103, 103, 109, 100, 223]
    """
    return [x + y for x, y in zip(l, l[1:])]


def incr_list_with_slice(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_with_slice([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [105, 103, 105, 102, 103, 103, 109, 100, 223]
    """
    return [x + y for x, y in zip(l, l[1:])]


def incr_list_with_slice_and_length(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_with_slice_and_length([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [105, 103, 105, 102, 103, 103, 109, 100, 223]
    """
    return [x + y for x, y in zip(l, l[1:])]


def incr_list_with_slice_and_index(l: list