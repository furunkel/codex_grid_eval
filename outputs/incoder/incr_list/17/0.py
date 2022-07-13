
def decr_list(l: list):
    """Return list with elements decremented by 2.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [3, 1, 3, 0, 1, 1, 7, -2, 121]
    """
    return [el - 2 for el in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 2.
    >>> decr_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
    {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
    """
    return {k: v - 2 for k, v in d.items()}


def decr_dict_by_key(
    d: dict, key: str, *, default: Optional[Any] = None
) -> Optional[Any]:
    """Return dict with elements decremented by 2 where key is key.
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'a')
    2
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'b')
    3
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'c')
    4
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'd')
    5
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'e')
    6
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'z')
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'z', default=1)
    1
    """
    return decr_dict_by_key_value(d, key, default, lambda x: x - 2)


def decr_dict_by_key_value(
    d: dict, key: str, default: Optional[Any] = None, func: Optional[Callable] = None
) -> Optional[Any]:
    """Return dict with elements decremented by 2 where key is key and value is value.
    >>> decr_dict_by_key_value({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'a', default=1)
    2
    >>> decr_dict_by_key_value({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'b')
    3
    >>> decr_dict_by_key_value({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'c')
    4
    >>> decr_dict_by_key_value({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'd')
    5
    >>> decr_dict_by_key_value({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'e')
    6
    >>> decr_dict_by_key_value({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 'z')
    >>> decr_dict_