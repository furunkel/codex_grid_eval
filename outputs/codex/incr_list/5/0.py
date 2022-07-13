
def incr_list(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [7, 5, 7, 4, 5, 5, 11, 2, 125]
    """
    return [x + 2 for x in l]


def even_list(l: list):
    """Return list with even elements.
    >>> even_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2, 0, 123]
    """
    return [x for x in l if x % 2 == 0]


def even_list_2(l: list):
    """Return list with even elements.
    >>> even_list_2([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2, 0, 123]
    """
    return list(filter(lambda x: x % 2 == 0, l))


def even_list_3(l: list):
    """Return list with even elements.
    >>> even_list_3([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2, 0, 123]
    """
    return list(filter(lambda x: x % 2 == 0, l))


def even_list_4(l: list):
    """Return list with even elements.
    >>> even_list_4([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2, 0, 123]
    """
    return list(filter(lambda x: x % 2 == 0, l))


def even_list_5(l: list):
    """Return list with even elements.
    >>> even_list_5([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2, 0, 123]
    """
    return list(filter(lambda x: x % 2 == 0, l))


def even_list_6(l: list):
    """Return list with even elements.
    >>> even_list_6([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [2, 0, 123]
    """
    return list(filter(lambda x: x % 2 == 0, l))


def even_list_7(l: list):
    """Return list with even elements.
    >>> even_list_7([5