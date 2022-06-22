
def decr_list(l: list):
    """Return list with elements decremented by 0.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """
    return [x - 1 for x in l]


def decr_list_2(l: list):
    """Return list with elements decremented by 0.
    >>> decr_list_2([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """
    return [x - 1 for x in l if x > 0]


def decr_list_3(l: list):
    """Return list with elements decremented by 0.
    >>> decr_list_3([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """
    return [x - 1 for x in l if x > 0 and x % 2 == 0]


def decr_list_4(l: list):
    """Return list with elements decremented by 0.
    >>> decr_list_4([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """
    return [x - 1 for x in l if x > 0 and x % 2 == 0 and x % 3 == 0]


def decr_list_5(l: list):
    """Return list with elements decremented by 0.
    >>> decr_list_5([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """
    return [x - 1 for x in l if x > 0 and x % 2 == 0 and x % 3 == 0 and x % 5 == 0]


def decr_list_6(l: list):
    """Return list with elements decremented by 0.
    >>> decr_list_6([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """
    return [x - 1 for x in