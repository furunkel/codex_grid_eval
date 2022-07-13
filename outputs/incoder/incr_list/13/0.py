
def decr_list(l: list):
    """Return list with elements decremented by 0.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """
    return [el - 1 for el in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 0.
    >>> decr_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    """
    return {k: el - 1 for k, el in d.items()}


def decr_dict_by_key(
    d: dict, key: str, default: Optional[Any] = None
) -> Optional[Any]:
    """Return dict with elements decremented by 0 by key.
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'a')
    1
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'b')
    2
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'c')
    3
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'd')
    4
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'e')
    5
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'z')
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'z', default=0)
    0
    """
    return d.get(key, default) - 1 if d.get(key) is not None else default


def decr_dict_by_key_list(
    d: dict, keys: list, default: Optional[Any] = None
) -> Optional[Any]:
    """Return dict with elements decremented by 0 by key.
    >>> decr_dict_by_key_list({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, ['a', 'b'])
    1
    >>> decr_dict_by_key_list({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, ['c', 'd'])
    3
    >>> decr_dict_by_key_list({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, ['e'])
    5
    >>> decr_dict_by_key_list({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, ['z'])
    >>> decr_dict_by_key_list({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, ['z'], default=0)
    0
    """
    return decr_dict_by_key(d, keys[0], default) if len(keys) == 1 else decr_dict_by_key(
        d, keys[0], decr_