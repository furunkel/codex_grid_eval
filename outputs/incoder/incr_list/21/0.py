
def decr_list(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [-9994, -9996, -9994, -9997, -9996, -9996, -9990, -9999, -9876]
    """
    return [x - 9999 for x in l]


@njit
def decr_dict(d: dict):
    """Return dict with elements decremented by 9999.
    >>> decr_dict({'a': 5, 'b': 3, 'c': 3, 'd': 2, 'e': 3, 'f': 9, 'g': 0})
    {'a': -9994, 'b': -9996, 'c': -9994, 'd': -9997, 'e': -9996, 'f': -9996, 'g': -9990}
    """
    return {k: x - 9999 for k, v in d.items()}


@njit
def decr_dict_list(d: dict):
    """Return dict with elements decremented by 9999.
    >>> decr_dict_list({'a': [5, 3], 'b': [3, 3], 'c': [3, 3], 'd': [2, 2], 'e': [3, 3], 'f': [9, 0], 'g': [0, 0]})
    {'a': [-9994, -9996], 'b': [-9994, -9996], 'c': [-9994, -9996], 'd': [-9997, -9996], 'e': [-9997, -9996], 'f': [-9996, -9990], 'g': [-9990, -9999]}
    """
    return {k: decr_list(v) for k, v in d.items()}


@njit
def decr_dict_list_dict(d: dict):
    """Return dict with elements decremented by 9999.
    >>> decr_dict_list_dict({'a': [5, 3], 'b': [3, 3], 'c': [3, 3], 'd': [2, 2], 'e': [3, 3], 'f': [9, 0], 'g': [0, 0]})
    {'a': {'a': -9994, 'b': -9996}, 'b': {'a': -9994, 'b': -9996}, 'c': {'a': -9994, 'b': -9996}, 'd': {'a': -9997, -9996}, 'e': {'a': -9997, -9996}, 'f': {'a': -9996, -9990}, 'g': {'a': -9990, -9999}}
    """
    return {k: decr_dict(v) for k, v in d.items()}


@njit
def decr_dict_list_dict_list(d: dict):
    """Return dict with elements decremented by 9999.
    >>> decr_dict_list_dict_list({'a': [5, 3], 'b': [3, 3], 'c': [3, 3], 'd': [2, 2], 'e': [3, 3], 'f': [9, 0], 'g': [0, 0]})
    {'a': {'a': [-9994, -9996]}, 'b': {'a': [-9994, -9996]}, 'c': {'a': [-9994, -9996]}, 'd': {'a': [-9997, -9996]}, 'e': {'