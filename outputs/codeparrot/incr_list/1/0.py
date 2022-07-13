
def incr_list(l: list):
    """Return list with elements incremented by 0.
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """

def incr_list_with_index(l: list, index: int):
    """Return list with elements incremented by index.
    >>> incr_list_with_index([5, 3, 5, 2, 3, 3, 9, 0, 123], 0)
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """

def incr_list_with_index_with_value(l: list, index: int, value: int):
    """Return list with elements incremented by index and value.
    >>> incr_list_with_index_with_value([5, 3, 5, 2, 3, 3, 9, 0, 123], 0, 123)
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """

def incr_list_with_index_with_value_and_index(l: list, index: int, value: int, index_value: int):
    """Return list with elements incremented by index and value.
    >>> incr_list_with_index_with_value_and_index([5, 3, 5, 2, 3, 3, 9, 0, 123], 0, 123, index_value=123)
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """

def incr_list_with_index_with_value_and_index_with_index_with_value(l: list, index: int, value: int, index_value: int, index_value_value: int):
    """Return list with elements incremented by index and value.
    >>> incr_list_with_index_with_value_and_index_with_value([5, 3, 5, 2, 3, 3, 9, 0, 123], 0, 123, index_value=123, index_value_value=123)
    [5, 3, 5, 2, 3, 3