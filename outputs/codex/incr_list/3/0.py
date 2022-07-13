
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]


def even_list(l: list):
    """Return list with even elements.
    >>> even_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2]
    """
    return [x for x in l if x % 2 == 0]


def even_list_2(l: list):
    """Return list with even elements.
    >>> even_list_2([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2]
    """
    return list(filter(lambda x: x % 2 == 0, l))


def even_list_3(l: list):
    """Return list with even elements.
    >>> even_list_3([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2]
    """
    return list(filter(lambda x: x % 2 == 0, l))


def even_list_4(l: list):
    """Return list with even elements.
    >>> even_list_4([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2]
    """
    return list(filter(lambda x: x % 2 == 0, l))


def even_list_5(l: list):
    """Return list with even elements.
    >>> even_list_5([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2]
    """
    return list(filter(lambda x: x % 2 == 0, l))


def even_list_6(l: list):
    """Return list with even elements.
    >>> even_list_6([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2]
    """
    return list(filter(lambda x: x % 2 == 0, l))


def even_list_7(l: list):
    """Return list with even elements.
    >>> even_list_7([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2]
   