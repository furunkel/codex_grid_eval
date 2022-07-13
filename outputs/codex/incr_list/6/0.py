
def incr_list(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list([1, 2, 3])
    [101, 102, 103]
    """
    return [x + 100 for x in l]

def incr_list_2(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_2([1, 2, 3])
    [101, 102, 103]
    """
    return list(map(lambda x: x + 100, l))

def incr_list_3(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_3([1, 2, 3])
    [101, 102, 103]
    """
    return list(map(add_100, l))

def incr_list_4(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_4([1, 2, 3])
    [101, 102, 103]
    """
    return list(map(lambda x: add_100(x), l))

def incr_list_5(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_5([1, 2, 3])
    [101, 102, 103]
    """
    return list(map(add_100, l))

def incr_list_6(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_6([1, 2, 3])
    [101, 102, 103]
    """
    return list(map(lambda x: add_100(x), l))

def incr_list_7(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_7([1, 2, 3])
    [101, 102, 103]
    """
    return list(map(add_100, l))

def incr_list_8(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list_8([1, 2, 3])
    [101, 102, 103]
    """
    return list(map(lambda x: add_100(x), l))

def incr_list_9(l: list