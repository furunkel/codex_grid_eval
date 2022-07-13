
def decr_list(l: list):
    """Return list with elements decremented by 1.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [4, 2, 4, 1, 2, 2, 8, -1, 122]
    """
    return [x - 1 for x in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 1.
    >>> decr_dict({'a': 5, 'b': 5, 'c': 3, 'd': 3, 'e': 2, 'f': 2, 'g': 1, 'h': 1})
    {'a': 4, 'b': 3, 'c': 2, 'd': 2, 'e': 1, 'f': 1, 'g': 0, 'h': 0}
    """
    return {k: v - 1 for k, v in d.items()}


def decr_dict_by_key(
    d: dict, key: str, value: Optional[int] = None
) -> Optional[dict]:
    """Return dict with elements decremented by 1 by key.
    >>> decr_dict_by_key({'a': 5, 'b': 5, 'c': 3, 'd': 3, 'e': 2, 'f': 2, 'g': 1, 'h': 1}, 'a')
    {'a': 4, 'b': 3, 'c': 2, 'd': 2, 'e': 1, 'f': 1, 'g': 0, 'h': 0}
    >>> decr_dict_by_key({'a': 5, 'b': 5, 'c': 3, 'd': 3, 'e': 2, 'f': 2, 'g': 1, 'h': 1}, 'e')
    {'a': 5, 'b': 4, 'c': 3, 'd': 3, 'e': 2, 'f': 2, 'g': 1, 'h': 1}
    """
    return {k: v - 1 if v is not None else v for k, v in d.items() if k == key}


def decr_dict_by_key_list(
    d: dict, keys: list, value: Optional[int] = None
) -> Optional[dict]:
    """Return dict with elements decremented by 1 by key.
    >>> decr_dict_by_key_list({'a': 5, 'b': 5, 'c': 3, 'd': 3, 'e': 2, 'f': 2, 'g': 1, 'h': 1}, [1, 2, 3])
    {'a': 4, 'b': 3, 'c': 2, 'd': 2, 'e': 1, 'f': 1, 'g': 0, 'h': 0}
    >>> decr_dict_by_key_list({'a': 5, 'b': 5, 'c': 3, 'd': 3, 'e': 2, 'f': 2, 'g': 1, 'h': 1}, [1, 2, 3])
    {'a': 4, 'b': 3, 'c': 2, 'd': 2, 'e': 1, 'f': 1, 'g': 0, 'h': 0}
    """
    return {k: v - 1 if v is not None else v for k, v in d.items() if k in keys}


def decr_dict_by_key_list_with_default(
    d: dict, keys: list, default: Optional[int] = None
) -> Optional[dict]:
    """Return dict with elements decremented by 1 by key.
    >>> decr_dict_by_key_list_with_default(
    ...     {'a': 5, 'b': 5, 'c': 3, 'd': 3, 'e': 2, 'f': 2, 'g': 1, 'h': 1},
    ...     [1, 2, 3],
    ...     default=None,
    ... )
    {'a': 4, 'b': 3, 'c': 2, 'd': 2, 'e': 1, 'f': 1, 'g': 0, 'h': 0}
    >>> decr_dict_by_key_list_with_default(
    ...     