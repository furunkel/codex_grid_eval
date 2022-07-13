
def decr_list(l: list):
    """Return list with elements decremented by 100.
    >>> decr_list([1, 2, 3])
    [-99, -98, -97]
    """
    return [el - 100 for el in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 100.
    >>> decr_dict({'a': 1, 'b': 2})
    {'a': -99, 'b': -98}
    """
    return {k: v - 100 for k, v in d.items()}


def decr_dict_by_key(
    d: dict, key: str, key_type: Optional[Callable] = None
) -> dict:
    """Return dict with elements decremented by 100.
    >>> decr_dict_by_key({'a': 1, 'b': 2}, 'a')
    {'a': -99, 'b': -98}
    """
    return {
        k: v - 100 if key_type is None else key_type(k) - 100
        for k, v in d.items()
        if key_type is None or key_type(k) == key
    }


def decr_dict_by_key_list(
    d: dict, keys: list, key_type: Optional[Callable] = None
) -> dict:
    """Return dict with elements decremented by 100.
    >>> decr_dict_by_key_list({'a': 1, 'b': 2}, [0, 1])
    {'a': -99, 'b': -98}
    """
    return {
        k: v - 100 if key_type is None else key_type(k) - 100
        for k, v in d.items()
        if key_type is None or key_type(k) in keys
    }


def decr_dict_by_key_list_with_default(
    d: dict, keys: list, defaults: dict, key_type: Optional[Callable] = None
) -> dict:
    """Return dict with elements decremented by 100.
    >>> decr_dict_by_key_list_with_default(
    ...     {'a': 1, 'b': 2}, [1], {'a': -99, 'b': -98}
    ... )
    {'a': -99, 'b': -98}
    """
    return {
        k: v - 100 if key_type is None else key_type(k) - 100
        for k, v in d.items()
        if key_type is None or key_type(k) in keys
    }


def decr_dict_by_key_list_with_default_list(
    d: dict, keys: list, defaults: list, key_type: Optional[Callable] = None
) -> dict:
    """Return dict with elements decremented by 100.
    >>> decr_dict_by_key_list_with_default_list(
    ...     {'a': 1, 'b': 2}, [1], {'a': -99, 'b': -98}
    ... )
    {'a': -99, 'b': -98}
    """
    return {
        k: v - 100 if key_type is None else key_type(k) - 100
        for k, v in d.items()
        if key_type is None or key_type(k) in keys
    }


def decr_dict_by_key_list_with_default_list_with_default(
    d: dict, keys: list, defaults: list, defaults_type: dict, key_type: Optional[Callable] = None
) -> 