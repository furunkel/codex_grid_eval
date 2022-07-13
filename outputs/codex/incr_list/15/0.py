
def decr_list(l: list):
    """Return list with elements decremented by 1.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [4, 2, 4, 1, 2, 2, 8, -1, 122]
    """
    return [x - 1 for x in l]


def decr_list_inplace(l: list):
    """Decrement each element of list by 1.
    >>> l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    >>> decr_list_inplace(l)
    >>> l
    [4, 2, 4, 1, 2, 2, 8, -1, 122]
    """
    for i in range(len(l)):
        l[i] -= 1


def decr_list_inplace_2(l: list):
    """Decrement each element of list by 1.
    >>> l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    >>> decr_list_inplace_2(l)
    >>> l
    [4, 2, 4, 1, 2, 2, 8, -1, 122]
    """
    for i, x in enumerate(l):
        l[i] = x - 1


def decr_list_inplace_3(l: list):
    """Decrement each element of list by 1.
    >>> l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    >>> decr_list_inplace_3(l)
    >>> l
    [4, 2, 4, 1, 2, 2, 8, -1, 122]
    """
    for i in range(len(l)):
        l[i] -= 1


def decr_list_inplace_4(l: list):
    """Decrement each element of list by 1.
    >>> l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    >>> decr_list_inplace_4(l)
    >>> l
    [4, 2, 4, 1, 2, 2, 8, -1, 122]
    """
    for i in range(len(l)):
        l[i] -= 1


def decr_list_inplace_5(l: list):
    """Decrement each element of list by 1.
    >>> l =