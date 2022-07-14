def decr_list(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [-9994, -9996, -9994, -9997, -9996, -9996, -9990, -9999, -9876]
    """
    return [x for x in l if x != -9999]


def decr_list_with_empty_elements(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list_with_empty_elements([])
    []
    """
    return [x for x in l if x != -9999]


def decr_list_with_non_empty_elements(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list_with_non_empty_elements([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [-9994, -9996, -9997, -9996, -9996, -9997, -9996, -9997, -9999, -9876]
    """
    return [x for x in l if x != -9999]


def decr_list_with_non_empty_elements_with_empty_elements(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list_with_non_empty_elements_with_empty_elements([])
    []
    """
    return [x for x in l if x != -9999]


def decr_list_with_non_empty_elements_with_empty_elements_with_empty_elements(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list_with_non_empty_elements_with_empty_elements([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [-9994, -9996, -9997, -9996, -9997, -9996, -9997, -9996, -9997, -9999, -9876]
    """
    return [x for x in l if x != -9999]


def decr_