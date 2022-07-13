
def decr_list(l: list):
    """Return list with elements decremented by 100.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [-95, -97, -95, -98, -97, -97, -91, -100, 23]
    """
    return [el - 100 for el in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 100.
    >>> decr_dict({5: -5, 3: -5, 2: -3, 9: -9, 0: 0, 123: 123})
    {-5: 5, -5: 7, -5: 5, -3: 5, -9: 7, -9: 1, -100: 12}
    """
    return {el - 100: el for el in d.values()}


def decr_dict_list(l: list):
    """Return list with elements decremented by 100.
    >>> decr_dict_list([{5: -5, 3: -5, 2: -3, 9: -9, 0: 0, 123: 123}])
    [{-5: 5, -5: 7, -5: 5, -3: 5, -9: 7, -9: 1, -100: 12}]
    """
    return [{el - 100: el} for el in l]


def decr_dict_dict(d: dict):
    """Return dict with elements decremented by 100.
    >>> decr_dict_dict({5: -5, 3: -5, 2: -3, 9: -9, 0: 0, 123: 123})
    {-5: 5, -5: 7, -5: 5, -3: 5, -9: 7, -9: 1, -100: 12}
    """
    return {el - 100: decr_dict(el) for el in d.values()}


def decr_dict_dict_list(l: list):
    """Return list with elements decremented by 100.
    >>> decr_dict_dict_list([{5: -5, 3: -5, 2: -3, 9: -9, 0: 0, 123: 123}])
    [{-5: 5, -5: 7, -5: 5, -3: 5, -9: 7, -9: 1, -100: 12}]
    """
    return [{el - 100: decr_dict_list(el) for el in l}]


def decr_dict_dict_dict(d: dict):
    """Return dict with elements decremented by 100.
    >>> decr_dict_dict_dict({5: -5, 3: -5, 2: -3, 9: -9, 0: 0, 123: 123})
    {-5: 5, -5: 7, -5: 5, -3: 5, -9: 7, -9: 1, -100: 12}
    """
    return {el - 100: decr_dict_dict(el) for el in d.values()}


def decr_dict_dict_dict_list(l: list):
    """Return list with elements decremented by 100.
    >>> decr_dict_dict_dict_list([{5: -5, 3: -5, 2: -3, 9: -9, 0: 0, 123: 123}])
    [{-5: 5, -5: 7, -5: 5, -3: 5, -9: 7, 